# 1️⃣ Create Dictionary
n = int(input("Enter number of key-value pairs: "))
my_dict = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

print("\nDictionary created:", my_dict)


# 2️⃣ Access Keys and Values
print("\nKeys:")
for key in my_dict.keys():
    print(key)

print("\nValues:")
for value in my_dict.values():
    print(value)


# 3️⃣ Add and Update Values
new_key = input("\nEnter new key to add: ")
new_value = input("Enter value: ")
my_dict[new_key] = new_value
print("After adding:", my_dict)

update_key = input("\nEnter key to update: ")
if update_key in my_dict:
    updated_value = input("Enter new value: ")
    my_dict[update_key] = updated_value
    print("After updating:", my_dict)
else:
    print("Key not found")


# 4️⃣ Delete Key
delete_key = input("\nEnter key to delete: ")
if delete_key in my_dict:
    del my_dict[delete_key]
    print("After deletion:", my_dict)
else:
    print("Key not found")


# 5️⃣ Count Number of Keys
count = 0
for _ in my_dict:
    count += 1

print("Total number of keys:", count)