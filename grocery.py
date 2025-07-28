num_items = int(input("Enter number of items: "))
total_cost = 0

for i in range(num_items):
    item = input(f"\nEnter name of item {i+1}: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    item_total = qty * price
    total_cost += item_total
    print(f"{item}: ₹{item_total:.2f}")

print(f"\nTotal Bill: ₹{total_cost:.2f}")
print("Thank you for shopping with us!")