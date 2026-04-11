# 🔹 DAY 11 - STRING & RECURSION


# 🔹 1. String Reverse (Recursion)
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]


# 🔹 2. Remove Duplicates
def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result


# 🔹 3. Check Sorted Array (Recursion)
def is_sorted(arr, index):
    if index == len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)


# 🔹 4. Generate Subsequences
def subsequences(s, current=""):
    if len(s) == 0:
        print(current)
        return

    # include character
    subsequences(s[1:], current + s[0])

    # exclude character
    subsequences(s[1:], current)


# 🔹 5. Permutations (Basic)
def permutations(s, current=""):
    if len(s) == 0:
        print(current)
        return

    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        permutations(remaining, current + ch)


# 🔹 MAIN PROGRAM

print("\n--- String Reverse ---")
print(reverse_string("hello"))


print("\n--- Remove Duplicates ---")
print(remove_duplicates("programming"))


print("\n--- Check Sorted Array ---")
arr = [1, 2, 3, 4]
print("Is Sorted:", is_sorted(arr, 0))


print("\n--- Subsequences ---")
subsequences("abc")


print("\n--- Permutations ---")
permutations("abc")