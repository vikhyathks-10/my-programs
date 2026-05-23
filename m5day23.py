# 🔹 DAY 23 - ARRAY & STRING LOGIC


# 🔹 1. Rotate Array

def rotate_array(arr, k):

    k = k % len(arr)

    return arr[-k:] + arr[:-k]


# 🔹 2. Merge Arrays

def merge_arrays(arr1, arr2):

    merged = arr1 + arr2

    return sorted(merged)


# 🔹 3. Move Zeros

def move_zeros(arr):

    result = []

    zeros = 0

    for num in arr:

        if num == 0:
            zeros += 1
        else:
            result.append(num)

    result.extend([0] * zeros)

    return result


# 🔹 4. Longest Word Finder

def longest_word(sentence):

    words = sentence.split()

    longest = max(words, key=len)

    return longest


# 🔹 5. Character Counter

def character_counter(text):

    freq = {}

    for ch in text:

        freq[ch] = freq.get(ch, 0) + 1

    return freq


# 🔹 MAIN PROGRAM

print("\n--- Rotate Array ---")

print(rotate_array([1, 2, 3, 4, 5], 2))


print("\n--- Merge Arrays ---")

print(merge_arrays([1, 3, 5], [2, 4, 6]))


print("\n--- Move Zeros ---")

print(move_zeros([0, 1, 0, 3, 12]))


print("\n--- Longest Word Finder ---")

sentence = "Python programming is powerful"

print(longest_word(sentence))


print("\n--- Character Counter ---")

print(character_counter("python"))