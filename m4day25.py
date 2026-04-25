# 🔹 DAY 25 - STRING PROBLEMS


# 🔹 1. Anagram Check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


# 🔹 2. Character Frequency
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# 🔹 3. Longest Substring Without Repeating Characters
def longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# 🔹 4. Palindrome Substring (Check existence)
def has_palindrome_substring(s):
    n = len(s)

    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > 1:
                return True
    return False


# 🔹 5. String Compression
def compress_string(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result


# 🔹 MAIN PROGRAM

print("\n--- Anagram ---")
print(is_anagram("listen", "silent"))


print("\n--- Character Frequency ---")
print(char_frequency("programming"))


print("\n--- Longest Substring ---")
print(longest_substring("abcabcbb"))


print("\n--- Palindrome Substring ---")
print(has_palindrome_substring("babad"))


print("\n--- String Compression ---")
print(compress_string("aaabbc"))