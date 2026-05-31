from preprocess import load_corpus, tokenize
from collections import defaultdict, Counter

# Build bigram model from corpus 
def build_bigram_model(tokens):
    """
    Returns a dict: {prev_word: Counter({next_word: count})}
    """
    bigrams = defaultdict(Counter)
    for i in range(len(tokens) - 1):
        bigrams[tokens[i]][tokens[i + 1]] += 1
    return bigrams

# Score a word given the previous word (context) 
def bigram_probability(word, prev_word, bigram_model, word_freq, total, alpha=1.0):
    """
    Smoothed probability: P(word | prev_word)
    alpha = Laplace smoothing factor
    vocab_size for smoothing
    """
    vocab_size = len(word_freq)
    context_count = sum(bigram_model[prev_word].values())

    if context_count == 0:
        # No context info, fall back to unigram probability
        return (word_freq[word] + alpha) / (total + alpha * vocab_size)

    return (bigram_model[prev_word][word] + alpha) / (context_count + alpha * vocab_size)

# Load once at import time
_text        = load_corpus()
_tokens      = tokenize(_text)
BIGRAM_MODEL = build_bigram_model(_tokens)

# Quick test 
if __name__ == "__main__":
    from preprocess import build_word_frequency
    from collections import Counter

    word_freq = build_word_frequency(_tokens)
    total     = sum(word_freq.values())

    # What word likely follows "the"?
    prev = "the"
    top5 = BIGRAM_MODEL[prev].most_common(5)
    print(f"Top 5 words after '{prev}': {top5}")

    # What word likely follows "good"?
    prev = "good"
    top5 = BIGRAM_MODEL[prev].most_common(5)
    print(f"Top 5 words after '{prev}': {top5}")

    # Compare probabilities
    print(f"\nP(world | the) = {bigram_probability('world', 'the', BIGRAM_MODEL, word_freq, total):.6f}")
    print(f"P(word  | the) = {bigram_probability('word',  'the', BIGRAM_MODEL, word_freq, total):.6f}")