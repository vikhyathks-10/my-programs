sentence = "Python is an amazing programming language"
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)
