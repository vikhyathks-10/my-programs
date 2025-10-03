arr = [1, 2, 2, 3, 1, 4, 2, 3]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print("Frequency of elements:", freq)
