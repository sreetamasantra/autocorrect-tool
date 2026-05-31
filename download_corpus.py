import urllib.request

url = "https://norvig.com/big.txt"
print("Downloading corpus...")
urllib.request.urlretrieve(url, "data/corpus.txt")
print("Done! Saved to data/corpus.txt")