# 🔹 DAY 4 - STRINGS INTERMEDIATE


# 🔹 1. Anagram Checker

def is_anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


# 🔹 2. Remove Duplicate Characters

def remove_duplicates(text):

    result = ""

    for ch in text:

        if ch not in result:
            result += ch

    return result


# 🔹 3. Longest Word Finder

def longest_word(sentence):

    words = sentence.split()

    longest = max(words, key=len)

    return longest


# 🔹 4. String Compression

def string_compression(text):

    compressed = ""

    count = 1

    for i in range(len(text)):

        if i < len(text) - 1 and text[i] == text[i + 1]:

            count += 1

        else:

            compressed += text[i] + str(count)

            count = 1

    return compressed


# 🔹 5. First Non-Repeating Character

def first_non_repeating(text):

    for ch in text:

        if text.count(ch) == 1:
            return ch

    return None


# 🔹 MAIN PROGRAM

print("🔹 Anagram Checker")
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))


print("\n🔹 Remove Duplicate Characters")
print(remove_duplicates("programming"))


print("\n🔹 Longest Word Finder")
sentence = "Python programming is very powerful"
print(longest_word(sentence))


print("\n🔹 String Compression")
print(string_compression("aaabbccccdd"))


print("\n🔹 First Non-Repeating Character")
print(first_non_repeating("aabbccddef"))