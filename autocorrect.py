from preprocess import load_corpus, tokenize, build_word_frequency
from collections import Counter
from ngram_model import BIGRAM_MODEL, bigram_probability

# Load corpus once at import time 
_text     = load_corpus()
_tokens   = tokenize(_text)
WORD_FREQ = build_word_frequency(_tokens)
VOCAB     = set(WORD_FREQ.keys())
TOTAL     = sum(WORD_FREQ.values())

# Edit Distance Operations 
def edits1(word):
    """All words 1 edit away from `word`."""
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [L + R[1:]           for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces   = [L + c + R[1:]       for L, R in splits if R for c in letters]
    inserts    = [L + c + R           for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    """All words 2 edits away (only keep known words to save time)."""
    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}

def known(words):
    """Filter to only words that exist in our vocabulary."""
    return {w for w in words if w in VOCAB}

def candidates(word):
    """
    Priority:
    1. word itself if already correct
    2. known words 1 edit away
    3. known words 2 edits away
    4. the original word (last resort)
    """
    return (known([word]) or
            known(edits1(word)) or
            known(edits2(word)) or
            {word})

# Probability scorer 
def probability(word):
    return WORD_FREQ[word] / TOTAL

# Main correction function
def correct_word(word):
    """Return the most probable correction for a single word."""
    word = word.lower()
    if word in VOCAB:
        return word   # already correct
    return max(candidates(word), key=probability)

# Context-aware sentence correction 
def correct_sentence(sentence):
    """Correct each word using bigram context from previous word."""
    words  = sentence.strip().split()
    result = []

    for i, word in enumerate(words):
        word = word.lower()
        if word in VOCAB:
            result.append(word)
            continue

        cands   = candidates(word)
        prev    = result[-1] if result else None

        if prev:
            # rank by bigram probability given previous word
            best = max(cands, key=lambda w: bigram_probability(
                w, prev, BIGRAM_MODEL, WORD_FREQ, TOTAL
            ))
        else:
            # first word — use unigram probability
            best = max(cands, key=probability)

        result.append(best)

    return ' '.join(result)

if __name__ == "__main__":
    tests = ["speling", "korrect", "waht", "hte wrold", "I hav a dreem"]
    for t in tests:
        print(f"  Input : {t}")
        print(f"  Output: {correct_sentence(t)}\n")