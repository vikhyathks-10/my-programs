# 🔹 DAY 9 - FREQUENCY PROBLEMS

from collections import Counter


# ==================================================
# 🔹 1. Frequency of Elements
# ==================================================

def frequency_of_elements(arr):

    freq = {}

    for num in arr:

        freq[num] = freq.get(num, 0) + 1

    return freq


# ==================================================
# 🔹 2. Most Frequent Element
# ==================================================

def most_frequent_element(arr):

    freq = Counter(arr)

    return max(freq, key=freq.get)


# ==================================================
# 🔹 3. Least Frequent Element
# ==================================================

def least_frequent_element(arr):

    freq = Counter(arr)

    return min(freq, key=freq.get)


# ==================================================
# 🔹 4. Frequency Sort
# ==================================================

def frequency_sort(arr):

    freq = Counter(arr)

    return sorted(arr,
                  key=lambda x: (-freq[x], x))


# ==================================================
# 🔹 5. Unique Elements Finder
# ==================================================

def unique_elements(arr):

    freq = Counter(arr)

    result = []

    for num in arr:

        if freq[num] == 1:
            result.append(num)

    return result


# ==================================================
# 🔹 MAIN PROGRAM
# ==================================================

arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]

print("Array:")
print(arr)


print("\n🔹 Frequency of Elements")
print(frequency_of_elements(arr))


print("\n🔹 Most Frequent Element")
print(most_frequent_element(arr))


print("\n🔹 Least Frequent Element")
print(least_frequent_element(arr))


print("\n🔹 Frequency Sort")
print(frequency_sort(arr))


print("\n🔹 Unique Elements Finder")
print(unique_elements(arr))