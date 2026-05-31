# ✍️ Autocorrect Tool

An AI-powered autocorrect system built with **Edit Distance** and **N-gram Language Modeling**, served via a **Flask** web application.

---

## 🚀 Features
- Corrects misspelled words using Levenshtein edit distance
- Uses bigram language model for context-aware corrections
- Highlights exactly which words were changed
- Clean, responsive web UI
- **90% accuracy** on standard spelling test set

---

## 🧠 How It Works
User Input → Tokenize → For each word:
├── Already correct? → Keep it
├── 1 edit away?     → Rank by bigram probability
└── 2 edits away?    → Rank by bigram probability
→ Return corrected sentence

### Models Used
| Model | Role |
|---|---|
| **Edit Distance (Levenshtein)** | Generates candidate corrections |
| **Unigram Frequency Model** | Ranks candidates by word frequency |
| **Bigram Language Model** | Ranks candidates using context (previous word) |

---

## 📁 Project Structure
autocorrect-tool/
├── data/
│   └── corpus.txt          # Peter Norvig's English corpus (1.1M tokens)
├── model/
│   └── init.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py                  # Flask backend
├── autocorrect.py          # Core correction engine
├── ngram_model.py          # Bigram language model
├── preprocess.py           # Corpus loading and tokenization
├── evaluate.py             # Accuracy evaluation script
├── download_corpus.py      # One-time corpus downloader
└── requirements.txt

---

## ⚙️ Setup & Run
```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/autocorrect-tool.git
cd autocorrect-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download corpus
python download_corpus.py

# 4. Run the app
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## 📊 Evaluation
```bash
python evaluate.py
```
| Metric | Score |
|---|---|
| Test cases | 20 |
| Correct | 18 |
| **Accuracy** | **90.0%** |

---

## 🛠️ Tech Stack
- **Python 3.x**
- **NLTK** — tokenization
- **Flask** — web framework
- **Vanilla JS + CSS** — frontend

---

## 📌 Dataset
[Peter Norvig's big.txt](https://norvig.com/big.txt) — ~1.1 million tokens of clean English text.

---

## 👩‍💻 Author
**Sreetama Santra** — B.Tech CSE(IoT), IEM Kolkata
