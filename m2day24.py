# Create first dictionary
n1 = int(input("Enter number of key-value pairs in first dictionary: "))
dict1 = {}

for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value (number): "))
    dict1[key] = value

print("\nDictionary 1:", dict1)


# 1️⃣ Check Key Exists
search_key = input("\nEnter key to check existence: ")

if search_key in dict1:
    print("Key exists in dictionary")
else:
    print("Key does not exist")


# Create second dictionary
n2 = int(input("\nEnter number of key-value pairs in second dictionary: "))
dict2 = {}

for i in range(n2):
    key = input("Enter key: ")
    value = int(input("Enter value (number): "))
    dict2[key] = value

print("Dictionary 2:", dict2)


# 2️⃣ Merge Two Dictionaries
merged = dict1.copy()
merged.update(dict2)
print("\nMerged Dictionary:", merged)


# 3️⃣ Find Maximum Value
max_value = None
max_key = None

for key in merged:
    if max_value is None or merged[key] > max_value:
        max_value = merged[key]
        max_key = key

print("Maximum value:", max_value)
print("Key with maximum value:", max_key)


# 4️⃣ Sort Dictionary by Key
sorted_by_key = dict(sorted(merged.items()))
print("\nDictionary sorted by key:", sorted_by_key)


# 5️⃣ Sort Dictionary by Value
sorted_by_value = dict(sorted(merged.items(), key=lambda item: item[1]))
print("Dictionary sorted by value:", sorted_by_value)