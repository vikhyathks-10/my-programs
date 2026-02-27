# =====================================
# 1️⃣ Inventory Management
# =====================================
inventory = {}

n = int(input("Enter number of products: "))
for i in range(n):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    inventory[product] = quantity

print("\nInventory:", inventory)

# Update stock
item = input("Enter product to update stock: ")
if item in inventory:
    new_qty = int(input("Enter new quantity: "))
    inventory[item] = new_qty
    print("Updated Inventory:", inventory)
else:
    print("Product not found")


# =====================================
# 2️⃣ ATM Data Using Dictionary
# =====================================
accounts = {
    "1001": {"Name": "Rahul", "Balance": 5000},
    "1002": {"Name": "Amit", "Balance": 8000}
}

acc_no = input("\nEnter account number: ")

if acc_no in accounts:
    print("Account Holder:", accounts[acc_no]["Name"])
    print("Balance:", accounts[acc_no]["Balance"])
else:
    print("Account not found")


# =====================================
# 3️⃣ Login System Using Dictionary
# =====================================
users = {
    "admin": "1234",
    "vikhyath": "python"
}

username = input("\nEnter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Login failed")


# =====================================
# 4️⃣ Menu-Driven Dictionary Program
# =====================================
data = {}

while True:
    print("\nDictionary Menu")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value

    elif choice == 2:
        key = input("Enter key to delete: ")
        if key in data:
            del data[key]
        else:
            print("Key not found")

    elif choice == 3:
        print("Dictionary:", data)

    elif choice == 4:
        break

    else:
        print("Invalid choice")


# =====================================
# 5️⃣ Count Vowels Using Dictionary
# =====================================
text = input("\nEnter a string: ").lower()
vowel_dict = {"a":0, "e":0, "i":0, "o":0, "u":0}

for ch in text:
    if ch in vowel_dict:
        vowel_dict[ch] += 1

print("Vowel Count:", vowel_dict)