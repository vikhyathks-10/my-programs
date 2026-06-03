# 🔹 DAY 3 - STRINGS BASICS


# 🔹 1. Reverse String

def reverse_string(text):

    return text[::-1]


# 🔹 2. Palindrome Check

def is_palindrome(text):

    text = text.lower()

    return text == text[::-1]


# 🔹 3. Count Vowels

def count_vowels(text):

    vowels = "aeiouAEIOU"

    count = 0

    for ch in text:

        if ch in vowels:
            count += 1

    return count


# 🔹 4. Count Words

def count_words(text):

    words = text.split()

    return len(words)


# 🔹 5. Find Character Frequency

def character_frequency(text):

    freq = {}

    for ch in text:

        freq[ch] = freq.get(ch, 0) + 1

    return freq


# 🔹 MAIN PROGRAM

text = "Python Programming"


print("Original String:")
print(text)


print("\nReverse String:")
print(reverse_string(text))


print("\nPalindrome Check:")

print("madam ->", is_palindrome("madam"))

print("python ->", is_palindrome("python"))


print("\nCount Vowels:")
print(count_vowels(text))


print("\nCount Words:")
print(count_words(text))


print("\nCharacter Frequency:")
print(character_frequency(text))