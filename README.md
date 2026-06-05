# Document Extraction Pipeline — Take-Home Exercise

## Context

You're completing a pipeline that takes legal documents (wills and trusts), classifies them, and extracts structured data using an LLM. The codebase is partially built — your job is to finish it.

The pipeline uses **OpenAI structured outputs** — you define Pydantic schemas and the API returns parsed, typed objects directly.

The pipeline works in two steps:
1. **Classify** the document as either a "will" or a "trust"
2. **Extract** structured fields (names, dates, assets, etc.) into a typed data object

## Quick Legal Primer

- A **will** says what happens to someone's property after they die. Key players:
  - **Testator** — the person whose will it is
  - **Executor** — the person who carries out the instructions (sometimes called "personal representative")
  - **Beneficiaries** — people who receive things

- A **trust** puts assets under the management of someone for the benefit of others. Key players:
  - **Grantor** (also called **Settlor**) — the person who creates the trust
  - **Trustee** — the person who manages it
  - **Beneficiaries** — people who benefit from the trust

- Both documents typically specify a governing **state**, an execution **date**, and the **assets** involved.

## What You Need To Do

1. **Define the classification schema** in `src/schemas.py`:
   - Complete the `ClassificationResult` Pydantic model

2. **Write the prompt templates** in `src/prompts.py`:
   - Classification prompt, will extraction prompt, trust extraction prompt

3. **Complete the `TODO` functions** in:
   - `src/classifier.py` — document classification
   - `src/extractor.py` — data extraction pipeline
   - `src/utils.py` — name and date normalization helpers

4. **Run the tests:**
   ```bash
   # Check your utility functions (no API calls needed)
   pytest tests/test_utils.py -v

   # Run the full extraction evaluation (requires OpenAI API key)
   python run_evaluation.py
   ```

5. **Target:** Score as high as you can. Perfect is possible.

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up your API key
cp .env.example .env
# Edit .env and add your OpenAI API key

# 3. Verify setup
pytest tests/test_utils.py -v
```

## Key Concept: Structured Outputs

This pipeline uses OpenAI's [structured outputs](https://platform.openai.com/docs/guides/structured-outputs). The `call_llm()` function in `client.py` accepts a Pydantic `BaseModel` class as `response_format` and returns a parsed instance of that model. The API guarantees the response conforms to the schema — no JSON parsing or cleanup needed on your end.

Look at `client.py` to see how this works, then look at `schemas.py` for the extraction schemas.

## Rules

- **You CAN modify:** `schemas.py` (the TODO section only), `classifier.py`, `extractor.py`, `utils.py`, `prompts.py`
- **You CANNOT modify:** `client.py`, `schemas.py` (below the "DO NOT MODIFY" line), test files, ground truth, or documents
- You can use any OpenAI model you want (the default is `gpt-4o-mini`)
- You can make as many API calls as you need per document

## Project Structure

```
├── README.md
├── requirements.txt
├── .env.example             # Copy to .env and add your OpenAI key
├── run_evaluation.py        # Scorecard runner (PROVIDED)
├── src/
│   ├── client.py            # OpenAI wrapper with structured outputs (PROVIDED — do not modify)
│   ├── schemas.py           # Pydantic models (HAS TODO for ClassificationResult)
│   ├── classifier.py        # Document classification (HAS TODOs)
│   ├── extractor.py         # Data extraction (HAS TODOs)
│   ├── utils.py             # Helper functions (HAS TODOs)
│   └── prompts.py           # Prompt templates (EMPTY — you write these)
├── documents/               # 6 test documents (plain text)
│   ├── doc_1.txt … doc_6.txt
├── ground_truth/            # Expected extraction outputs (JSON)
│   ├── doc_1.json … doc_6.json
└── tests/
    ├── test_utils.py        # Unit tests for utils (PROVIDED)
    └── test_extraction.py   # Extraction scoring tests (PROVIDED)
```

## What We Evaluate

1. **Extraction accuracy** — your automated score from `run_evaluation.py`
2. **Schema design** — how you define `ClassificationResult`
3. **Prompt quality** — we read your prompts in `prompts.py`
4. **Code quality** — we read your TODO completions
5. **Efficiency** — how many tokens and API calls you use per document
