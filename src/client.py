"""OpenAI client wrapper. DO NOT MODIFY THIS FILE."""

import os
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

_client = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _client


def call_llm(prompt: str, document_text: str, response_format: type[BaseModel], model: str = "gpt-4o-mini"):
    """Send a prompt + document to the LLM with structured output. Returns a parsed Pydantic object."""
    client = get_client()
    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": document_text},
        ],
        response_format=response_format,
    )
    return response.choices[0].message.parsed
