# English Spelling Corrector

A simple English spelling corrector implemented in Python as part of my NLP course.

## Features

- Word frequency-based vocabulary
- Levenshtein edit distance
- Candidate generation
- Candidate ranking
- Top-K spelling suggestions

## How It Works

```text
Input Word
    ↓
Vocabulary
    ↓
Edit Distance
    ↓
Candidate Generation
    ↓
Ranking
    ↓
Top-K Suggestions
```

## Candidates are ranked by:

- Edit distance
- Word frequency
- Alphabetical order
