sentence = "apple banana apple orange banana apple"
words = sentence.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Word Frequency:", freq)
