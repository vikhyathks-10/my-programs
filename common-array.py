arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
common = []

for num in arr1:
    if num in arr2 and num not in common:
        common.append(num)

print("Common Elements:", common)
