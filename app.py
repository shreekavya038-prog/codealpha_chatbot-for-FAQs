from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("faqs.json", "r", encoding="utf-8") as f:
    FAQS = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    q = data.get("question", "").lower().strip()

    if "python" in q:
        ans = "Python is a popular programming language."
    elif "flask" in q:
        ans = "Flask is a lightweight web framework for Python."
    elif "nlp" in q:
        ans = "NLP stands for Natural Language Processing."
    elif "github" in q:
        ans = "GitHub is a platform for hosting and sharing code."
    else:
        ans = "I don't know the answer. Try asking about Python, Flask, NLP, or GitHub."

    return jsonify({"answer": ans})

if __name__ == "__main__":
    app.run(debug=True)
