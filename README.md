# CAPTIER Dataset

## 1. Dataset Description

This is a threat intelligence entity relation extraction dataset in the APT (Advanced Persistent Threat) domain.

The data is collected from APT attack descriptions related to Groups in ATT&CK. This repository contains annotations for 1,500 instances, including **7,053 entities**, **5,907 relations**, and **388 unique triple types**.

## 2. Data Structure

The original annotations use the native relation data structure from the doccano annotation tool, stored in JSONL format. An expanded single-line example structure is as follows:

```json
{
    "text": "Google was founded on September 4, 1998, by Larry Page and Sergey Brin.",
    "entities": [
        {
            "id": 0,
            "start_offset": 0,
            "end_offset": 6,
            "label": "ORG"
        },
        {
            "id": 1,
            "start_offset": 22,
            "end_offset": 39,
            "label": "DATE"
        },
        {
            "id": 2,
            "start_offset": 44,
            "end_offset": 54,
            "label": "PERSON"
        },
        {
            "id": 3,
            "start_offset": 59,
            "end_offset": 70,
            "label": "PERSON"
        }
    ],
    "relations": [
        {
            "from_id": 0,
            "to_id": 1,
            "type": "foundedAt"
        },
        {
            "from_id": 0,
            "to_id": 2,
            "type": "foundedBy"
        },
        {
            "from_id": 0,
            "to_id": 3,
            "type": "foundedBy"
        }
    ]
}
```

This repository provides a conversion script to transform CAPTIER data into CoNLL-04 format directly.

### Quick Start

```bash
# 1. Install dependencies
pip install spacy
python -m spacy download en_core_web_lg

# 2. Save the converter code as doccano_to_conll04.py
# 3. Run the example
python -c "
from doccano_to_conll04 import convert_to_conll04
convert_to_conll04('input_dataset.jsonl', 'output_conll04.jsonl')
"
```

## 3. Dataset Statistics and Classification

### 3.1 Sentence and Word Statistics

| Metric | Value |
|--------|-------|
| Average words per sentence | 14.99 |
| Median word count | 14.0 |
| Maximum sentence length | 55 words |
| Minimum sentence length | 4 words |
| Empty annotation ratio | 0.0% |
| Maximum entities per sentence | 21 entities |

### 3.2 Entity Type Distribution

| Entity Type | Count |
|-------------|-------|
| Threat-Actor | 1,490 |
| Attack-Pattern | 1,472 |
| Infrastructure | 726 |
| Tool | 635 |
| Malware | 562 |
| Configuration | 416 |
| Identity | 396 |
| File | 393 |
| Observed-Data | 382 |
| Credential | 206 |
| Location | 141 |
| Industry | 117 |
| Vulnerability | 117 |

### 3.3 Entity Information Statistics

| Metric | Value |
|--------|-------|
| Total entities | 7,053 |
| Average words per entity | 1.90 |
| Median word count | 2 |
| Average entities per sentence | 4.70 |
| Median | 4.0 |
| Standard deviation | 1.84 |

### 3.4 Relation Type Distribution

| Relation Type | Count |
|---------------|-------|
| uses | 1,250 |
| requires | 1,095 |
| interacts-with | 827 |
| targets | 497 |
| attributed-to | 446 |
| related-to | 367 |
| exploits | 336 |
| has | 321 |
| affects | 301 |
| located-at | 295 |
| indicates | 98 |
| variant-of | 74 |

### 3.5 Relation Information Statistics

| Metric | Value |
|--------|-------|
| Total relations | 5,907 |
| Average relations per sentence | 3.94 |
| Median | 4.0 |
| Standard deviation | 2.19 |

## 4. Unique Triple Types and Counts

<details>
<summary>Click to expand the complete triple type statistics</summary>

| Head Entity Type | Relation Type | Tail Entity Type | Count |
|------------------|---------------|------------------|-------|
| Threat-Actor | uses | Attack-Pattern | 530 |
| Tool | uses | Attack-Pattern | 352 |
| Attack-Pattern | targets | Infrastructure | 138 |
| Attack-Pattern | requires | Infrastructure | 139 |
| Attack-Pattern | requires | Configuration | 152 |
| Threat-Actor | uses | Malware | 165 |
| Attack-Pattern | requires | Tool | 331 |
| Attack-Pattern | requires | Attack-Pattern | 127 |
| Threat-Actor | exploits | Configuration | 112 |
| Attack-Pattern | attributed-to | Threat-Actor | 103 |
| Attack-Pattern | targets | Identity | 104 |
| Attack-Pattern | interacts-with | Malware | 97 |
| Attack-Pattern | affects | Observed-Data | 96 |
| Attack-Pattern | requires | File | 65 |
| Attack-Pattern | requires | Credential | 64 |
| Identity | located-at | Location | 67 |
| Industry | located-at | Location | 70 |
| Threat-Actor | targets | Identity | 70 |
| Malware | uses | Attack-Pattern | 68 |
| Attack-Pattern | requires | Vulnerability | 26 |
| Attack-Pattern | affects | File | 58 |
| Threat-Actor | exploits | Infrastructure | 56 |
| Threat-Actor | targets | Industry | 57 |
| Threat-Actor | interacts-with | Tool | 54 |
| Threat-Actor | exploits | Credential | 52 |
| Threat-Actor | exploits | Vulnerability | 51 |
| Malware | variant-of | Malware | 50 |
| Attack-Pattern | interacts-with | File | 49 |
| Threat-Actor | interacts-with | Infrastructure | 48 |
| Threat-Actor | interacts-with | Malware | 47 |
| Threat-Actor | interacts-with | File | 43 |
| Infrastructure | attributed-to | Identity | 42 |
| Attack-Pattern | affects | Configuration | 42 |
| Attack-Pattern | related-to | Attack-Pattern | 40 |
| File | has | File | 38 |
| Tool | interacts-with | Infrastructure | 37 |
| Infrastructure | has | Infrastructure | 35 |
| Attack-Pattern | affects | Credential | 35 |
| Attack-Pattern | requires | Observed-Data | 33 |
| Threat-Actor | located-at | Location | 31 |
| Tool | interacts-with | File | 31 |
| File | located-at | Infrastructure | 31 |
| Observed-Data | attributed-to | Infrastructure | 30 |
| Threat-Actor | interacts-with | Configuration | 28 |
| Threat-Actor | related-to | Threat-Actor | 27 |
| Attack-Pattern | interacts-with | Tool | 26 |
| Attack-Pattern | interacts-with | Observed-Data | 26 |
| Infrastructure | related-to | Infrastructure | 25 |
| Attack-Pattern | interacts-with | Infrastructure | 25 |
| Threat-Actor | uses | File | 24 |
| Attack-Pattern | interacts-with | Configuration | 24 |
| Malware | attributed-to | Threat-Actor | 23 |
| Threat-Actor | interacts-with | Credential | 23 |
| Identity | related-to | Identity | 23 |
| Observed-Data | related-to | Observed-Data | 23 |
| Observed-Data | indicates | Infrastructure | 23 |
| Threat-Actor | targets | Location | 22 |
| Vulnerability | related-to | Vulnerability | 22 |
| Infrastructure | attributed-to | Infrastructure | 22 |
| Configuration | related-to | Observed-Data | 22 |
| Infrastructure | has | Observed-Data | 22 |
| Threat-Actor | interacts-with | Observed-Data | 22 |
| Attack-Pattern | exploits | Configuration | 21 |
| Threat-Actor | attributed-to | Identity | 21 |
| File | attributed-to | Infrastructure | 20 |
| Attack-Pattern | uses | Attack-Pattern | 20 |
| File | has | Malware | 20 |
| Malware | interacts-with | Infrastructure | 20 |
| Vulnerability | has | Vulnerability | 20 |
| Tool | variant-of | Tool | 19 |
| Attack-Pattern | affects | Identity | 18 |
| Configuration | related-to | Configuration | 18 |
| Attack-Pattern | interacts-with | Credential | 18 |
| Threat-Actor | uses | Observed-Data | 15 |
| Malware | has | Configuration | 15 |
| Threat-Actor | targets | Infrastructure | 15 |
| Credential | attributed-to | Identity | 15 |
| Credential | attributed-to | Infrastructure | 15 |
| File | interacts-with | Malware | 15 |
| Infrastructure | has | File | 15 |
| Observed-Data | indicates | File | 14 |
| Vulnerability | attributed-to | Infrastructure | 14 |
| Attack-Pattern | requires | Identity | 14 |
| Observed-Data | indicates | Malware | 14 |
| File | related-to | File | 14 |
| Tool | interacts-with | Observed-Data | 14 |
| Observed-Data | has | Observed-Data | 14 |
| Attack-Pattern | exploits | Vulnerability | 14 |
| Tool | located-at | Infrastructure | 13 |
| Observed-Data | attributed-to | Identity | 13 |
| Industry | attributed-to | Industry | 13 |
| Configuration | located-at | Infrastructure | 13 |
| Infrastructure | has | Malware | 12 |
| Attack-Pattern | targets | Credential | 12 |
| Tool | uses | Attack-Pattern | 12 |
| Malware | interacts-with | File | 12 |
| File | has | Observed-Data | 12 |
| Malware | interacts-with | Configuration | 12 |
| Observed-Data | located-at | Infrastructure | 12 |
| Malware | located-at | Infrastructure | 12 |
| Attack-Pattern | targets | Industry | 12 |
| File | has | Configuration | 11 |
| Malware | affects | Identity | 11 |
| Malware | interacts-with | Observed-Data | 11 |
| Malware | targets | Infrastructure | 11 |
| Attack-Pattern | has | Attack-Pattern | 11 |
| Attack-Pattern | affects | Infrastructure | 11 |
| Identity | attributed-to | Identity | 10 |
| Threat-Actor | uses | Infrastructure | 10 |
| Attack-Pattern | uses | Malware | 10 |
| Infrastructure | located-at | Location | 10 |
| Attack-Pattern | targets | Tool | 10 |
| Threat-Actor | requires | Attack-Pattern | 9 |
| Malware | exploits | Credential | 9 |
| Identity | indicates | Threat-Actor | 9 |
| Observed-Data | indicates | Tool | 9 |
| Tool | attributed-to | Tool | 9 |
| Configuration | attributed-to | Infrastructure | 9 |
| Threat-Actor | affects | Observed-Data | 9 |
| Malware | uses | Tool | 9 |
| File | attributed-to | Identity | 8 |
| Observed-Data | indicates | Identity | 8 |
| Malware | interacts-with | Malware | 8 |
| Malware | related-to | Tool | 8 |
| Tool | related-to | Tool | 8 |
| Attack-Pattern | affects | Tool | 8 |
| Malware | related-to | File | 8 |
| Observed-Data | related-to | Infrastructure | 8 |
| Threat-Actor | has | Tool | 7 |
| Malware | targets | Identity | 7 |
| Credential | related-to | Credential | 7 |
| Tool | has | Tool | 7 |
| Identity | interacts-with | Malware | 7 |
| Malware | uses | File | 7 |
| Threat-Actor | attributed-to | Threat-Actor | 6 |
| Tool | has | Observed-Data | 6 |
| Identity | has | Infrastructure | 6 |
| Infrastructure | has | Configuration | 6 |
| Malware | requires | Attack-Pattern | 6 |
| Tool | requires | Configuration | 6 |
| Threat-Actor | interacts-with | Attack-Pattern | 6 |
| Configuration | interacts-with | Configuration | 6 |
| Identity | interacts-with | Observed-Data | 6 |
| Observed-Data | indicates | Attack-Pattern | 6 |
| Threat-Actor | has | Malware | 6 |
| Threat-Actor | interacts-with | Identity | 6 |
| Identity | has | Credential | 5 |
| Malware | has | Observed-Data | 5 |
| Tool | interacts-with | Credential | 5 |
| Configuration | has | Observed-Data | 5 |
| Attack-Pattern | interacts-with | Identity | 5 |
| Malware | requires | Credential | 5 |
| Credential | located-at | Infrastructure | 5 |
| Infrastructure | interacts-with | Infrastructure | 5 |
| Identity | has | Configuration | 5 |
| Threat-Actor | related-to | Identity | 5 |
| Observed-Data | indicates | Configuration | 5 |
| Identity | related-to | Infrastructure | 5 |
| Observed-Data | related-to | File | 4 |
| Threat-Actor | related-to | Attack-Pattern | 4 |
| Tool | attributed-to | Identity | 4 |
| File | has | Credential | 4 |
| Attack-Pattern | related-to | Identity | 4 |
| Attack-Pattern | exploits | Credential | 4 |
| Malware | interacts-with | Tool | 4 |
| File | interacts-with | File | 4 |
| Malware | attributed-to | Malware | 4 |
| Vulnerability | affects | Infrastructure | 4 |
| Configuration | has | Configuration | 4 |
| File | interacts-with | Configuration | 4 |
| Threat-Actor | requires | Configuration | 4 |
| Identity | has | Observed-Data | 4 |
| Industry | has | Industry | 4 |
| Configuration | related-to | File | 4 |
| Configuration | located-at | Configuration | 4 |
| Attack-Pattern | targets | Configuration | 4 |
| Tool | has | Configuration | 4 |
| Infrastructure | related-to | Identity | 3 |
| Tool | targets | Infrastructure | 3 |
| Identity | targets | Infrastructure | 3 |
| Attack-Pattern | uses | Tool | 3 |
| Infrastructure | interacts-with | Malware | 3 |
| Threat-Actor | uses | Credential | 3 |
| Malware | uses | Infrastructure | 3 |
| Infrastructure | attributed-to | Industry | 3 |
| Threat-Actor | exploits | Tool | 3 |
| Configuration | attributed-to | Identity | 3 |
| Credential | has | Observed-Data | 3 |
| Vulnerability | attributed-to | Tool | 3 |
| Malware | has | Malware | 3 |
| Malware | located-at | File | 3 |
| Infrastructure | located-at | Infrastructure | 3 |
| Threat-Actor | uses | Configuration | 3 |
| Industry | related-to | Identity | 3 |
| Credential | related-to | Infrastructure | 3 |
| Configuration | attributed-to | Observed-Data | 3 |
| Infrastructure | interacts-with | File | 3 |
| Malware | exploits | Configuration | 3 |
| Malware | targets | File | 3 |
| Configuration | related-to | Infrastructure | 2 |
| Attack-Pattern | related-to | Malware | 2 |
| Location | attributed-to | Location | 2 |
| Malware | targets | Location | 2 |
| Configuration | related-to | Identity | 2 |
| Identity | related-to | Observed-Data | 2 |
| Tool | requires | Attack-Pattern | 2 |
| Identity | indicates | Identity | 2 |
| Identity | related-to | Threat-Actor | 2 |
| Attack-Pattern | related-to | Tool | 2 |
| Configuration | related-to | Malware | 2 |
| Attack-Pattern | related-to | Configuration | 2 |
| Tool | related-to | Identity | 2 |
| Configuration | interacts-with | Credential | 2 |
| Tool | interacts-with | Tool | 2 |
| Credential | interacts-with | Infrastructure | 2 |
| Credential | related-to | Configuration | 2 |
| Identity | interacts-with | File | 2 |
| Credential | related-to | Identity | 2 |
| Identity | related-to | Configuration | 2 |
| Observed-Data | located-at | File | 2 |
| Observed-Data | attributed-to | File | 2 |
| Malware | related-to | Infrastructure | 2 |
| Observed-Data | related-to | Configuration | 2 |
| Tool | related-to | Configuration | 2 |
| Malware | related-to | Configuration | 2 |
| File | uses | Attack-Pattern | 2 |
| Attack-Pattern | related-to | Infrastructure | 2 |
| Malware | variant-of | Tool | 2 |
| Observed-Data | related-to | Identity | 2 |
| Identity | located-at | Infrastructure | 2 |
| Tool | related-to | File | 2 |
| Observed-Data | located-at | Malware | 2 |
| Malware | targets | Industry | 2 |
| Configuration | related-to | Tool | 2 |
| Malware | attributed-to | File | 2 |
| Identity | attributed-to | Infrastructure | 2 |
| Malware | requires | Infrastructure | 2 |
| Tool | requires | Credential | 2 |
| Credential | related-to | Observed-Data | 2 |
| Threat-Actor | requires | Tool | 2 |
| File | attributed-to | File | 2 |
| Observed-Data | interacts-with | Observed-Data | 2 |
| Attack-Pattern | related-to | Credential | 2 |
| Configuration | has | Credential | 2 |
| Configuration | related-to | Credential | 2 |
| Observed-Data | affects | Credential | 2 |
| Malware | requires | Tool | 2 |
| File | related-to | Credential | 2 |
| Configuration | interacts-with | Tool | 2 |
| File | interacts-with | Tool | 2 |
| Attack-Pattern | targets | Vulnerability | 2 |
| Attack-Pattern | exploits | Infrastructure | 2 |
| Configuration | attributed-to | Malware | 2 |
| Credential | attributed-to | Credential | 2 |
| Infrastructure | attributed-to | Configuration | 2 |
| Attack-Pattern | has | File | 2 |
| Attack-Pattern | has | Observed-Data | 2 |
| Observed-Data | related-to | Credential | 2 |
| Attack-Pattern | variant-of | Attack-Pattern | 2 |
| Configuration | interacts-with | Infrastructure | 2 |
| Malware | uses | Observed-Data | 2 |
| Malware | requires | Observed-Data | 2 |
| Attack-Pattern | related-to | Observed-Data | 2 |
| Configuration | affects | Observed-Data | 2 |
| File | related-to | Observed-Data | 2 |
| Vulnerability | located-at | Infrastructure | 2 |
| Malware | requires | Identity | 2 |
| Industry | attributed-to | Identity | 2 |
| Credential | attributed-to | Configuration | 2 |
| Observed-Data | attributed-to | Tool | 2 |
| Malware | related-to | Attack-Pattern | 2 |
| File | interacts-with | Infrastructure | 2 |
| Malware | requires | Malware | 2 |
| Infrastructure | related-to | Observed-Data | 2 |
| Tool | uses | File | 1 |
| Identity | related-to | Attack-Pattern | 1 |
| Malware | targets | Credential | 1 |
| Identity | related-to | Malware | 1 |
| Identity | uses | File | 1 |
| Identity | uses | Infrastructure | 1 |
| Identity | uses | Tool | 1 |
| Observed-Data | affects | Identity | 1 |
| Identity | related-to | Tool | 1 |
| Observed-Data | interacts-with | Threat-Actor | 1 |
| Infrastructure | uses | Infrastructure | 1 |
| Observed-Data | indicates | Threat-Actor | 1 |
| Threat-Actor | variant-of | Malware | 1 |
| Identity | indicates | Identity | 1 |
| Malware | related-to | Identity | 1 |
| Tool | indicates | Malware | 1 |
| Vulnerability | attributed-to | Configuration | 1 |
| Malware | related-to | Observed-Data | 1 |
| Threat-Actor | exploits | Identity | 2 |
| Identity | attributed-to | Attack-Pattern | 2 |
| Identity | indicates | Attack-Pattern | 1 |
| Credential | attributed-to | Configuration | 2 |
| Infrastructure | attributed-to | Attack-Pattern | 1 |
| Infrastructure | has | Vulnerability | 2 |
| Configuration | interacts-with | Identity | 1 |
| Identity | interacts-with | Configuration | 1 |
| Identity | interacts-with | Infrastructure | 1 |
| Infrastructure | related-to | Credential | 1 |
| Tool | has | Infrastructure | 1 |
| Threat-Actor | attributed-to | Attack-Pattern | 1 |
| Malware | has | File | 1 |
| Malware | requires | Configuration | 4 |
| Infrastructure | related-to | Tool | 3 |
| Tool | attributed-to | Infrastructure | 1 |
| Observed-Data | attributed-to | Malware | 1 |
| Infrastructure | related-to | Attack-Pattern | 1 |
| Configuration | related-to | Attack-Pattern | 1 |
| Infrastructure | attributed-to | Tool | 1 |
| Credential | related-to | Identity | 1 |
| File | located-at | Location | 1 |
| Infrastructure | targets | Observed-Data | 1 |
| Infrastructure | requires | Observed-Data | 1 |
| Tool | requires | File | 1 |
| File | has | Vulnerability | 1 |
| Credential | attributed-to | File | 1 |
| Attack-Pattern | interacts-with | Vulnerability | 1 |
| Observed-Data | indicates | Observed-Data | 1 |
| Tool | exploits | Infrastructure | 1 |
| Attack-Pattern | related-to | File | 1 |
| Identity | attributed-to | Threat-Actor | 1 |
| Attack-Pattern | attributed-to | Malware | 1 |
| Configuration | interacts-with | Malware | 1 |
| Attack-Pattern | attributed-to | Attack-Pattern | 1 |
| Configuration | located-at | Tool | 1 |
| Threat-Actor | targets | Credential | 1 |
| Malware | targets | Tool | 1 |
| Tool | related-to | Malware | 1 |
| File | attributed-to | Attack-Pattern | 1 |
| Malware | related-to | Malware | 1 |
| Malware | uses | Configuration | 1 |
| Credential | located-at | File | 1 |
| Tool | interacts-with | Vulnerability | 1 |
| Tool | interacts-with | Identity | 1 |
| Tool | interacts-with | Industry | 1 |
| Malware | affects | Configuration | 1 |
| Malware | located-at | Observed-Data | 3 |
| Credential | located-at | Observed-Data | 1 |
| Configuration | indicates | Observed-Data | 1 |
| Configuration | located-at | Observed-Data | 1 |
| Infrastructure | related-to | Configuration | 1 |
| Tool | exploits | Configuration | 1 |
| Threat-Actor | attributed-to | Location | 1 |
| Threat-Actor | requires | File | 1 |
| File | indicates | Observed-Data | 1 |
| Configuration | interacts-with | Observed-Data | 1 |
| Infrastructure | related-to | File | 1 |
| Threat-Actor | related-to | Malware | 1 |
| File | indicates | Threat-Actor | 1 |
| File | interacts-with | Credential | 1 |
| Observed-Data | requires | Attack-Pattern | 1 |
| Malware | exploits | Vulnerability | 1 |
| Threat-Actor | requires | Infrastructure | 1 |
| Tool | requires | Identity | 1 |
| Credential | interacts-with | Observed-Data | 1 |
| Threat-Actor | affects | Infrastructure | 1 |
| Threat-Actor | affects | Industry | 1 |
| Credential | interacts-with | Malware | 1 |
| Malware | located-at | Location | 1 |
| Malware | attributed-to | Infrastructure | 1 |
| Credential | located-at | Malware | 1 |
| Credential | attributed-to | Attack-Pattern | 1 |
| Observed-Data | interacts-with | File | 1 |
| Observed-Data | located-at | Tool | 1 |
| Configuration | requires | Credential | 1 |
| File | related-to | Attack-Pattern | 1 |
| Infrastructure | targets | Identity | 1 |
| Attack-Pattern | interacts-with | Attack-Pattern | 1 |
| Identity | related-to | File | 1 |
| Tool | requires | Tool | 1 |
| Tool | interacts-with | Attack-Pattern | 1 |
| Identity | indicates | Location | 1 |
| Attack-Pattern | affects | Location | 1 |
| Location | located-at | Infrastructure | 1 |
| Attack-Pattern | targets | Observed-Data | 2 |

</details>

## 5. Overlapping Entity Types and Counts

| Source Entity Type | Target Entity Type | Count |
|--------------------|-------------------|-------|
| Attack-Pattern | File | 122 |
| Attack-Pattern | Observed-Data | 105 |
| Attack-Pattern | Malware | 78 |
| Attack-Pattern | Configuration | 70 |
| Attack-Pattern | Infrastructure | 66 |
| Attack-Pattern | Credential | 47 |
| Attack-Pattern | Identity | 38 |
| Attack-Pattern | Tool | 34 |
| Attack-Pattern | Vulnerability | 4 |
| Attack-Pattern | Location | 1 |

---
