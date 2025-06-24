# Doccano to CoNLL04 Converter - Complete Setup and Usage Guide

## 1. Prerequisites and Installation

### Install Required Libraries

```bash
# Install spaCy
pip install spacy

# Download the English language model (large version)
python -m spacy download en_core_web_lg

# Alternative: If you have storage constraints, you can use the smaller model
# python -m spacy download en_core_web_sm
```

### Verify Installation

```python
import spacy
print("spaCy version:", spacy.__version__)

# Check if model is installed
if spacy.util.is_package("en_core_web_lg"):
    print("✅ en_core_web_lg model is installed")
else:
    print("❌ en_core_web_lg model is NOT installed")
```

## 2. Sample Input Data

Create a file named `input_dataset.jsonl` with the following sample data:

```json
{"id": "doc_001", "text": "Apple Inc. was founded by Steve Jobs in Cupertino, California.", "entities": [{"id": "ent_1", "start_offset": 0, "end_offset": 10, "label": "ORG"}, {"id": "ent_2", "start_offset": 25, "end_offset": 35, "label": "PER"}, {"id": "ent_3", "start_offset": 39, "end_offset": 48, "label": "LOC"}, {"id": "ent_4", "start_offset": 50, "end_offset": 60, "label": "LOC"}], "relations": [{"type": "founded_by", "from_id": "ent_1", "to_id": "ent_2"}, {"type": "located_in", "from_id": "ent_1", "to_id": "ent_3"}]}
{"id": "doc_002", "text": "Microsoft Corporation is headquartered in Redmond, Washington.", "entities": [{"id": "ent_5", "start_offset": 0, "end_offset": 21, "label": "ORG"}, {"id": "ent_6", "start_offset": 43, "end_offset": 50, "label": "LOC"}, {"id": "ent_7", "start_offset": 52, "end_offset": 62, "label": "LOC"}], "relations": [{"type": "located_in", "from_id": "ent_5", "to_id": "ent_6"}]}
{"id": "doc_003", "text": "Google was co-founded by Larry Page and Sergey Brin at Stanford University.", "entities": [{"id": "ent_8", "start_offset": 0, "end_offset": 6, "label": "ORG"}, {"id": "ent_9", "start_offset": 25, "end_offset": 35, "label": "PER"}, {"id": "ent_10", "start_offset": 40, "end_offset": 51, "label": "PER"}, {"id": "ent_11", "start_offset": 55, "end_offset": 75, "label": "ORG"}], "relations": [{"type": "founded_by", "from_id": "ent_8", "to_id": "ent_9"}, {"type": "founded_by", "from_id": "ent_8", "to_id": "ent_10"}]}
```

## 3. Running the Converter

### Basic Usage

```python
from doccano_to_conll04 import convert_to_conll04

# Convert the dataset
convert_to_conll04("input_dataset.jsonl", "output_conll04.jsonl")
```

### Complete Example Script

```python
#!/usr/bin/env python3
"""
Complete example script for converting Doccano format to CoNLL04 format
"""
import json
import os
from doccano_to_conll04 import convert_to_conll04

def create_sample_data():
    """Create sample input data for testing"""
    sample_data = [
        {
            "id": "doc_001",
            "text": "Apple Inc. was founded by Steve Jobs in Cupertino, California.",
            "entities": [
                {"id": "ent_1", "start_offset": 0, "end_offset": 10, "label": "ORG"},
                {"id": "ent_2", "start_offset": 25, "end_offset": 35, "label": "PER"},
                {"id": "ent_3", "start_offset": 39, "end_offset": 48, "label": "LOC"},
                {"id": "ent_4", "start_offset": 50, "end_offset": 60, "label": "LOC"}
            ],
            "relations": [
                {"type": "founded_by", "from_id": "ent_1", "to_id": "ent_2"},
                {"type": "located_in", "from_id": "ent_1", "to_id": "ent_3"}
            ]
        },
        {
            "id": "doc_002",
            "text": "Microsoft Corporation is headquartered in Redmond, Washington.",
            "entities": [
                {"id": "ent_5", "start_offset": 0, "end_offset": 21, "label": "ORG"},
                {"id": "ent_6", "start_offset": 43, "end_offset": 50, "label": "LOC"},
                {"id": "ent_7", "start_offset": 52, "end_offset": 62, "label": "LOC"}
            ],
            "relations": [
                {"type": "located_in", "from_id": "ent_5", "to_id": "ent_6"}
            ]
        }
    ]
    
    with open("input_dataset.jsonl", "w", encoding="utf-8") as f:
        for item in sample_data:
            f.write(json.dumps(item) + "\n")
    
    print("✅ Sample data created: input_dataset.jsonl")

def verify_output():
    """Verify the conversion output"""
    if not os.path.exists("output_conll04.jsonl"):
        print("❌ Output file not found!")
        return
    
    print("✅ Conversion completed! Output file: output_conll04.jsonl")
    print("\nSample output:")
    with open("output_conll04.jsonl", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if i <= 2:  # Show first 2 lines
                data = json.loads(line)
                print(f"Document {i}:")
                print(f"  Tokens: {data['tokens']}")
                print(f"  Entities: {data['entities']}")
                print(f"  Relations: {data['relations']}")
                print()

if __name__ == "__main__":
    print("🚀 Starting Doccano to CoNLL04 conversion example...")
    
    # Step 1: Create sample data
    create_sample_data()
    
    # Step 2: Run conversion
    print("🔄 Converting data...")
    convert_to_conll04("input_dataset.jsonl", "output_conll04.jsonl")
    
    # Step 3: Verify output
    verify_output()
    
    print("✨ Example completed successfully!")
```

## 4. Expected Output Format

The output file `output_conll04.jsonl` will contain data in the following format:

```json
{"tokens": ["Apple", "Inc.", "was", "founded", "by", "Steve", "Jobs", "in", "Cupertino", ",", "California", "."], "entities": [{"type": "ORG", "start": 0, "end": 2}, {"type": "PER", "start": 5, "end": 7}, {"type": "LOC", "start": 8, "end": 9}, {"type": "LOC", "start": 10, "end": 11}], "relations": [{"type": "founded_by", "head": 0, "tail": 1}, {"type": "located_in", "head": 0, "tail": 2}], "orig_id": "doc_001"}
```

## 5. Troubleshooting

### Common Issues and Solutions

1. **spaCy model not found**
   ```bash
   python -m spacy download en_core_web_lg
   ```

2. **Memory issues with large datasets**
   - The script includes garbage collection (`gc.collect()`) to manage memory
   - Process files in smaller batches if needed

3. **Invalid entity offsets**
   - The script includes validation and will skip invalid entities
   - Check the console output for detailed error messages

4. **JSON parsing errors**
   - Ensure input file is valid JSONL format (one JSON object per line)
   - Check for encoding issues (use UTF-8)

## 6. File Structure

```
project/
├── doccano_to_conll04.py    # Main converter script
├── input_dataset.jsonl      # Input data (Doccano format)
├── output_conll04.jsonl     # Output data (CoNLL04 format)
└── example_runner.py        # Complete example script
```

Run the example with:
```bash
python example_runner.py
```
