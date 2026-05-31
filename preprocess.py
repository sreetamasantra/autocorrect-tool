import re
from collections import Counter

def load_corpus(filepath="data/corpus.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def tokenize(text):
    # Extract only lowercase words
    return re.findall(r'[a-z]+', text.lower())

def build_word_frequency(tokens):
    return Counter(tokens)

def get_vocabulary(word_freq):
    return set(word_freq.keys())

if __name__ == "__main__":
    text = load_corpus()
    tokens = tokenize(text)
    word_freq = build_word_frequency(tokens)
    vocab = get_vocabulary(word_freq)

    print(f"Total tokens     : {len(tokens):,}")
    print(f"Unique vocabulary: {len(vocab):,}")
    print(f"Top 10 words     : {word_freq.most_common(10)}")