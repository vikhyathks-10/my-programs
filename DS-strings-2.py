# 1. Find all substrings of a string
s = input("Enter a string: ")

print("All substrings:")
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])

# 2. Remove duplicate characters from a string
result = ""
for ch in s:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)

# 3. Find the longest word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()

longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

# 4. Implement string compression (aaabb → a3b2)
compressed = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        compressed += s[i - 1] + str(count)
        count = 1

compressed += s[-1] + str(count)
print("Compressed string:", compressed)

# 5. Convert a string to integer (atoi)
num_str = input("Enter a numeric string: ")
num = 0

for ch in num_str:
    num = num * 10 + (ord(ch) - ord('0'))

print("Integer value:", num)
