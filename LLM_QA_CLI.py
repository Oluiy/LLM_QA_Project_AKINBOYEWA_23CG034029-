#!/usr/bin/env python3
"""LLM_QA_CLI.py

Simple CLI for asking natural language questions to an LLM API (OpenAI by default).

Usage: set environment variable `OPENAI_API_KEY` before running to enable real API calls.
"""
import os
import re
import sys
import json
from typing import List

try:
    import google.generativeai as genai
except Exception:
    genai = None


def preprocess(text: str) -> List[str]:
    # Basic preprocessing: lowercase, remove punctuation, tokenize on whitespace
    text = text.lower()
    # remove punctuation (keep alphanumerics and spaces)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = [t for t in text.split() if t]
    return tokens


def construct_prompt(original: str, tokens: List[str]) -> str:
    return (
        "You are a helpful assistant. Answer concisely and accurately.\n"
        f"Original question: {original}\n"
        f"Processed tokens: {' '.join(tokens)}\n"
        "Provide a clear answer and, when helpful, a short rationale."
    )


def call_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or genai is None:
        # Fallback / simulation when API not configured
        return (
            "[No API key configured or `google-generativeai` package missing] "
            "Simulated response: I received your question and would answer it here."
        )

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Error calling Gemini API] {e}"


def main():
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        try:
            question = input("Enter your question: ")
        except KeyboardInterrupt:
            print("\nGoodbye")
            return

    if not question.strip():
        print("No question provided. Exiting.")
        return

    tokens = preprocess(question)
    prompt = construct_prompt(question, tokens)

    print("\n--- Processed Question ---")
    print("Tokens:", " ".join(tokens))
    print("\n--- Sending to LLM API ---")

    answer = call_gemini(prompt)

    print("\n--- Answer ---")
    print(answer)


if __name__ == "__main__":
    main()
