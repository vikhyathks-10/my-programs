laptops = [
    {"name": "HP Pavilion", "price": 45000},
    {"name": "Dell Inspiron", "price": 52000},
    {"name": "Lenovo ThinkPad", "price": 60000},
    {"name": "Asus VivoBook", "price": 40000},
]

min_price = int(input("Enter minimum price: "))
max_price = int(input("Enter maximum price: "))

print("\nLaptops in your range:")
found = False
for laptop in laptops:
    if min_price <= laptop["price"] <= max_price:
        print(f"{laptop['name']} - ₹{laptop['price']}")
        found = True

if not found:
    print("❌ No laptops found in this range.")
print("\nThank you for using the Laptop Builder!")