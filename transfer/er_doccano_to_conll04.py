import json
import spacy
import traceback
from pathlib import Path
import gc  

def convert_to_conll04(input_file, output_file):
    try:
        # Verify if the model exists
        if not spacy.util.is_package("en_core_web_lg"):
            raise ValueError("spaCy model 'en_core_web_lg' not installed")
        nlp = spacy.blank("en")  # Use basic tokenization only
        # Keep only tokenization functionality
    except Exception as e:
        print(f"Model loading failed: {str(e)}")
        return

    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Input file does not exist: {input_file}")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f_in, \
                open(output_file, 'w', encoding='utf-8') as f_out:

            for line_num, line in enumerate(f_in, 1):
                if not line.strip():
                    # Add detailed logging at entity validation (around line 30 in original code)
                    print(
                        f"Invalid entity text fragment: '{text[ent_start:ent_end]}' | Original text length: {len(text)} | Entity span: {ent_start}-{ent_end}")
                    continue

                try:
                    doc = json.loads(line)
                    text = doc.get('text', '')
                    orig_id = doc.get('id', '')
                    # Guard against empty text
                    if not text:
                        print(f"Line {line_num}: Skipping empty text")
                        continue

                    # Validate text length and entity offsets
                    text_len = len(text)
                    for entity in doc.get('entities', []):
                        start = entity.get('start_offset', -1)
                        end = entity.get('end_offset', -1)
                        if start < 0 or end > text_len or start >= end:
                            print(f"Line {line_num}: Invalid entity offset start={start}, end={end}, text_len={text_len}")
                            continue

                    # Use spaCy for tokenization
                    spacy_doc = nlp(text)
                    tokens = []
                    token_spans = []

                    # Safely generate token_spans
                    for token in spacy_doc:
                        token_length = len(token.text)
                        end_pos = token.idx + token_length
                        if token.idx < 0 or end_pos > len(text):
                            continue
                        tokens.append(token.text)
                        token_spans.append((token.idx, end_pos))

                    # Explicitly release spaCy document
                    del spacy_doc
                    gc.collect()
                    
                    # Create entity mapping table (original entity ID -> converted entity index)
                    entity_map = {}
                    conll_entities = []

                    # Process each entity
                    for entity in doc['entities']:
                        ent_start = entity['start_offset']
                        ent_end = entity['end_offset']
                        label = entity['label']
                        # Added offset validity check
                        if ent_start < 0 or ent_end > len(text) or ent_start >= ent_end:
                            print(
                                f"Line {line_num}: Skipping invalid entity - start={ent_start}, end={ent_end}, text_len={len(text)}")
                            continue  # Skip this entity directly
                        
                        # Find token indices that overlap with the entity
                        overlapping = []
                        for idx, (tok_start, tok_end) in enumerate(token_spans):
                            # Check if token overlaps with entity
                            if max(tok_start, ent_start) < min(tok_end, ent_end):
                                overlapping.append(idx)

                        if not overlapping:
                            continue

                        # Determine entity boundaries (consecutive tokens)
                        start_idx = min(overlapping)
                        end_idx = max(overlapping) + 1  # End index is exclusive

                        conll_entities.append({
                            "type": label,
                            "start": start_idx,
                            "end": end_idx
                        })

                        # Record mapping from original ID to new index
                        entity_map[entity['id']] = len(conll_entities) - 1

                    # Process relations
                    conll_relations = []
                    for relation in doc.get('relations', []):
                        head_id = relation['from_id']
                        tail_id = relation['to_id']

                        if head_id in entity_map and tail_id in entity_map:
                            conll_relations.append({
                                "type": relation['type'],
                                "head": entity_map[head_id],
                                "tail": entity_map[tail_id]
                            })

                    # Build CoNLL04 format
                    conll_doc = {
                        "tokens": tokens,
                        "entities": conll_entities,
                        "relations": conll_relations,
                        "orig_id": orig_id
                    }

                    f_out.write(json.dumps(conll_doc) + '\n')
                except json.JSONDecodeError:
                    print(f"Line {line_num}: JSON parsing failed")
                except Exception as e:
                    print(f"Line {line_num} processing failed: {str(e)}")
                    traceback.print_exc()
    except IOError as e:
        print(f"File operation failed: {str(e)}")

# Usage example
if __name__ == "__main__":
    convert_to_conll04("input_dataset.jsonl", "output_conll04.jsonl")