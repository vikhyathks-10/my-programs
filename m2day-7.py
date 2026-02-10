# 1️⃣ Count characters in a string
text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Total characters:", count)


# 2️⃣ Count vowels and consonants
vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# 3️⃣ Count words in a string
words = text.split()
print("Number of words:", len(words))


# 4️⃣ Reverse a string
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Reversed string:", reverse)


# 5️⃣ Check palindrome string
if text == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")
