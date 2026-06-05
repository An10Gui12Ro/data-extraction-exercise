"""
Run all documents through the extraction pipeline and print a scorecard.

Usage: python run_evaluation.py
"""

import json
import os
import sys
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
    return 1.0 if predicted.strip().lower() == expected.strip().lower() else 0.0


def score_name_list(predicted: list, expected: list) -> float:
    pred_normalized = {normalize_name(n).lower() for n in predicted}
    exp_normalized = {normalize_name(n).lower() for n in expected}
    if not exp_normalized:
        return 1.0 if not pred_normalized else 0.0
    intersection = pred_normalized & exp_normalized
    precision = len(intersection) / len(pred_normalized) if pred_normalized else 0.0
    recall = len(intersection) / len(exp_normalized)
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)


def score_asset_list(predicted: list, expected: list) -> float:
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


def format_score(score: float) -> str:
    if score == 1.0:
        return "PASS"
    elif score == 0.0:
        return "FAIL"
    else:
        return f"{score:.0%}"


def main():
    doc_files = sorted(f for f in os.listdir(DOCS_DIR) if f.endswith(".txt"))

    if not doc_files:
        print("No documents found in documents/")
        sys.exit(1)

    print("\n=== Document Extraction Scorecard ===\n")

    all_scores = []

    for doc_file in doc_files:
        doc_text = load_doc(doc_file)
        truth = load_truth(doc_file)

        try:
            result = process_document(doc_text)
        except Exception as e:
            print(f"{doc_file} ({truth['document_type']})")
            print(f"  ERROR: {e}")
            print()
            all_scores.append(0.0)
            continue

        doc_type_correct = result.document_type == truth["document_type"]

        scores = {}
        scores["document_type"] = 1.0 if doc_type_correct else 0.0
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
        all_scores.append(avg_score)

        print(f"{doc_file} ({truth['document_type']})")
        for field, score in scores.items():
            label = f"  {field}:"
            print(f"{label:<20} {format_score(score)}")
        print(f"  {'-> Score:':<19} {avg_score:.0%}")
        print()

    overall = sum(all_scores) / len(all_scores) if all_scores else 0.0
    print("=" * 36)
    print(f"OVERALL SCORE: {overall:.0%}")
    print("=" * 36)
    print()


if __name__ == "__main__":
    main()
