from flask import Flask, request, jsonify, render_template
from autocorrect import correct_sentence, VOCAB

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/correct", methods=["POST"])
def correct():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Empty input"}), 400

    corrected = correct_sentence(text)

    # Preserve original capitalization of first letter
    if text[0].isupper():
        corrected = corrected[0].upper() + corrected[1:]

    # Find which words were changed
    original_words  = text.lower().split()
    corrected_words = corrected.lower().split()
    changes = [
        {"original": o, "corrected": c}
        for o, c in zip(original_words, corrected_words)
        if o != c
    ]

    return jsonify({
        "original":  text,
        "corrected": corrected,
        "changes":   changes
    })

@app.route("/check_word", methods=["POST"])
def check_word():
    """Check if a single word is in vocabulary."""
    data = request.get_json()
    word = data.get("word", "").lower().strip()
    return jsonify({"known": word in VOCAB})

if __name__ == "__main__":
    app.run(debug=True)