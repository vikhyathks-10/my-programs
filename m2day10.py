text = input("Enter a string: ")

# 1️⃣ Check Anagram
s1 = input("\nEnter first string for anagram check: ")
s2 = input("Enter second string for anagram check: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not anagram")


# 2️⃣ String Compression (aaabb → a3b2)
compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1

if len(text) > 0:
    compressed += text[-1] + str(count)

print("\nCompressed string:", compressed)


# 3️⃣ Remove Duplicate Characters
unique = ""
for ch in text:
    if ch not in unique:
        unique += ch

print("Without duplicates:", unique)


# 4️⃣ First Non-Repeating Character
char_count = {}

for ch in text:
    char_count[ch] = char_count.get(ch, 0) + 1

first_non_repeat = None
for ch in text:
    if char_count[ch] == 1:
        first_non_repeat = ch
        break

if first_non_repeat:
    print("First non-repeating character:", first_non_repeat)
else:
    print("No non-repeating character found")


# 5️⃣ Most Frequent Character
max_char = None
max_count = 0

for ch in char_count:
    if char_count[ch] > max_count:
        max_count = char_count[ch]
        max_char = ch

print("Most frequent character:", max_char)
