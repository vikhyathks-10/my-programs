text = "Hello World"
print("Original String:", text)

vowels = "aeiouAEIOU"
result = ''.join([char for char in text if char not in vowels])

print("String without vowels:", result)
