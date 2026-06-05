"""
Extraction accuracy tests. DO NOT MODIFY THIS FILE.

Run with: pytest tests/test_extraction.py -v
Or use: python run_evaluation.py (for a nicer scorecard)
"""

import json
import os
import pytest
from src.extractor import process_document
from src.utils import normalize_name

DOCS_DIR = "documents"
TRUTH_DIR = "ground_truth"


def load_doc(name):
    with open(os.path.join(DOCS_DIR, name), "r") as f:
        return f.read()


def load_truth(name):
    json_name = name.replace(".txt", ".json")
    with open(os.path.join(TRUTH_DIR, json_name), "r") as f:
        return json.load(f)


def score_string(predicted: str, expected: str) -> float:
    """Score a single string field. Returns 1.0 for match, 0.0 for mismatch."""
    return 1.0 if predicted.strip().lower() == expected.strip().lower() else 0.0


def score_name_list(predicted: list, expected: list) -> float:
    """Score a list of names using normalized comparison. Returns 0-1."""
    pred_normalized = {normalize_name(n).lower() for n in predicted}
    exp_normalized = {normalize_name(n).lower() for n in expected}
    if not exp_normalized:
        return 1.0 if not pred_normalized else 0.0
    intersection = pred_normalized & exp_normalized
    precision = len(intersection) / len(pred_normalized) if pred_normalized else 0.0
    recall = len(intersection) / len(exp_normalized)
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)  # F1


def score_asset_list(predicted: list, expected: list) -> float:
    """Score assets with fuzzy matching. Each expected asset gets a match score."""
    if not expected:
        return 1.0 if not predicted else 0.0
    if not predicted:
        return 0.0
    scores = []
    for exp_asset in expected:
        exp_words = set(exp_asset.lower().split())
        best = 0.0
        for pred_asset in predicted:
            pred_words = set(pred_asset.lower().split())
            overlap = len(exp_words & pred_words) / len(exp_words | pred_words)
            best = max(best, overlap)
        scores.append(best)
    return sum(scores) / len(scores)


# Generate individual test cases per document
doc_files = sorted(f for f in os.listdir(DOCS_DIR) if f.endswith(".txt"))


@pytest.mark.parametrize("doc_file", doc_files)
def test_document_extraction(doc_file):
    doc_text = load_doc(doc_file)
    truth = load_truth(doc_file)
    result = process_document(doc_text)

    # Check document type
    assert result.document_type == truth["document_type"], \
        f"Classification failed: got {result.document_type}, expected {truth['document_type']}"

    # Score each field
    scores = {}
    scores["date"] = score_string(result.date, truth["date"])
    scores["state"] = score_string(result.state, truth["state"])

    if truth["document_type"] == "will":
        scores["testator"] = score_string(
            normalize_name(result.testator), normalize_name(truth["testator"])
        )
        scores["executors"] = score_name_list(result.executors, truth["executors"])
        scores["assets"] = score_asset_list(result.assets, truth["assets"])
    else:
        scores["grantors"] = score_name_list(result.grantors, truth["grantors"])
        scores["trustees"] = score_name_list(result.trustees, truth["trustees"])
        scores["assets"] = score_asset_list(result.assets, truth["assets"])

    avg_score = sum(scores.values()) / len(scores)
    print(f"\n  {doc_file}: {avg_score:.0%} — {scores}")
    assert avg_score >= 0.5, f"Score too low: {avg_score:.0%}"
