from flask import Flask, render_template, request
import os
import re

try:
    import google.generativeai as genai
except Exception:
    genai = None

app = Flask(__name__)


def preprocess(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = [t for t in text.split() if t]
    return tokens


def construct_prompt(original: str, tokens):
    return (
        "You are a helpful assistant. Answer concisely and accurately.\n"
        f"Original question: {original}\n"
        f"Processed tokens: {' '.join(tokens)}\n"
        "Provide a clear answer and, when helpful, a short rationale."
    )


def call_gemini(prompt: str):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or genai is None:
        return "[No API key configured or `google-generativeai` package missing] Simulated response."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Error calling Gemini API] {e}"


@app.route("/", methods=["GET", "POST"])
def index():
    processed = None
    answer = None
    question = ""
    if request.method == "POST":
        question = request.form.get("question", "").strip()
        tokens = preprocess(question)
        processed = " ".join(tokens)
        prompt = construct_prompt(question, tokens)
        answer = call_gemini(prompt)
    return render_template("index.html", question=question, processed=processed, answer=answer)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
