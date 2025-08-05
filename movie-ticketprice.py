num_tickets = int(input("Enter the number of tickets: "))
ticket_price = float(input("Enter price of one ticket: "))

total = num_tickets * ticket_price
if num_tickets > 5:
    discount = total * 0.10
    total = total - discount
    print(f"Discount applied: ₹{discount}")

print(f"Total cost = ₹{total}")
