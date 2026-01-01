# 1. Reverse a string without using slicing
s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed string:", rev)

# 2. Check if a string is palindrome
if s == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# 3. Count vowels and consonants
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# 4. Find first non-repeating character
found = False
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character:", ch)
        found = True
        break

if not found:
    print("No non-repeating character found")

# 5. Check if two strings are anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
