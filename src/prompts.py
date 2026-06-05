"""
Prompt templates for document classification and extraction.

YOUR TASK: Write the prompt strings below. These are sent as the system message
to the LLM. The document text is sent as the user message. The LLM response is
automatically parsed into the corresponding Pydantic schema via structured outputs.

Requirements:
- CLASSIFICATION_PROMPT should guide the LLM to classify a document as "will" or "trust"
- WILL_EXTRACTION_PROMPT should guide the LLM to extract data matching the WillExtraction schema
- TRUST_EXTRACTION_PROMPT should guide the LLM to extract data matching the TrustExtraction schema

Refer to schemas.py for the exact field names and expected formats.
"""

CLASSIFICATION_PROMPT = ""
# TODO: Write a prompt that classifies a document as either "will" or "trust".
# The response schema enforces the output structure — your prompt should guide
# the LLM to make the right classification.

WILL_EXTRACTION_PROMPT = ""
# TODO: Write a prompt that extracts structured data from a will document.
# The response will be parsed into a WillExtraction object.
# Pay attention to date format (YYYY-MM-DD), state (full name), executor names, etc.
# Note: some documents use "personal representative" instead of "executor" — same role.

TRUST_EXTRACTION_PROMPT = ""
# TODO: Write a prompt that extracts structured data from a trust document.
# The response will be parsed into a TrustExtraction object.
# Important: extract only CURRENT trustees, not successor trustees.
# Note: some documents use "Settlor" instead of "Grantor" — same role.
# Pay attention to date format (YYYY-MM-DD), state (full name), grantor names, etc.
