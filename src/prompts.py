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

CLASSIFICATION_PROMPT = """
You are a legal document classifier. Your task is to determine whether a given document is a "will" or a "trust".

- A will is a legal document that specifies how a person's property should be distributed after their death. It typically uses phrases like "Last Will and Testament", names a Testator, and appoints an Executor or Personal Representative.
- A trust is a legal document that places assets under the management of a Trustee for the benefit of others. It typically uses phrases like "Declaration of Trust" or "Trust Agreement", and names a Grantor or Settlor and a Trustee.

Classify the document as exactly "will" or "trust".
"""
# TODO: Write a prompt that classifies a document as either "will" or "trust".
# The response schema enforces the output structure — your prompt should guide
# the LLM to make the right classification.

WILL_EXTRACTION_PROMPT = """
You are a legal document data extractor. Extract structured information from the provided will document.

Rules:
- document_type: Always "will".
- testator: The full name of the person whose will it is (the one declaring the will).
- executors: A list of full names of all appointed executor(s). Some documents call this role "Personal Representative" — treat it as the same role. If the document appoints Co-Executors, include all of them. Do NOT include alternate or successor executors.
- assets: Extract a list of specific assets being distributed. 
    • Each asset must be a short, clean and concise description.
    • Focus only on the key identifying information (property address, account type with last digits, vehicle model/year, etc.).
    • Good examples: 
        - "Real property located at 742 Evergreen Terrace, Springfield, Illinois"
        - "Chase Bank checking account ending in 4521"
        - "2019 Honda Accord"
        - "Investment portfolio at Fidelity Investments ending in 8834"
        • Bad examples (do not do this): "all funds held in my Chase Bank...", "the condominium unit and all furnishings...".
    • Do NOT include residuary estate clauses (e.g. "the rest of my estate").
    • Include specific charitable bequests as separate assets.
- date: The execution date of the document in YYYY-MM-DD format.
- state: The governing state as a full name (e.g. "Illinois", not "IL").
"""
# TODO: Write a prompt that extracts structured data from a will document.
# The response will be parsed into a WillExtraction object.
# Pay attention to date format (YYYY-MM-DD), state (full name), executor names, etc.
# Note: some documents use "personal representative" instead of "executor" — same role.

TRUST_EXTRACTION_PROMPT = """
You are a legal document data extractor. Extract structured information from the provided trust document.

Rules:
- document_type: Always "trust".
- grantors: A list of full names of the grantor(s). Some documents use "Settlor" instead of "Grantor" — treat it as the same role.
- trustees: A list of full names of the CURRENT (initial) trustee(s) only. Do NOT include successor trustees or alternate trustees.
- assets: Extract a list of specific assets in the trust.
    • Each asset must be a short, clean and concise description as it appears in the document or Schedule A.
    • Focus only on the key identifying information.
    • Good examples:
        - "Real property located at 3847 Riverside Drive, Austin, Texas 78704"
        - "Wells Fargo savings account ending in 7893"
        - "Vanguard investment account ending in 5541"
    • Do not add extra phrases like "all funds held in..." or "together with all improvements...".
    • Keep each asset as one clean line/item.
- date: The execution date of the document in YYYY-MM-DD format.
- state: The governing state as a full name (e.g. "Texas", not "TX").
"""
# TODO: Write a prompt that extracts structured data from a trust document.
# The response will be parsed into a TrustExtraction object.
# Important: extract only CURRENT trustees, not successor trustees.
# Note: some documents use "Settlor" instead of "Grantor" — same role.
# Pay attention to date format (YYYY-MM-DD), state (full name), grantor names, etc.
