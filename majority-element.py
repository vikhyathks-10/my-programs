arr = [3, 3, 4, 2, 3, 3, 5, 3]
print("Array:", arr)

n = len(arr)
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

majority = None
for key, value in freq.items():
    if value > n // 2:
        majority = key
        break

if majority:
    print("Majority Element:", majority)
else:
    print("No Majority Element")
