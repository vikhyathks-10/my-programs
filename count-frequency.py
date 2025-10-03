text = "hello world"
char_freq = {}

for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

print("Character Frequency:", char_freq)
