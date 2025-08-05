gst_rate = 18  

items = []
while True:
    name = input("Enter item name (or 'stop' to finish): ")
    if name.lower() == "stop":
        break
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    items.append((name, qty, price))

print("\n------- INVOICE -------")
total = 0
for name, qty, price in items:
    line_total = qty * price
    total += line_total
    print(f"{name:<15} Qty:{qty:<3} Price:{price:<7} Total:{line_total}")

gst_amount = total * gst_rate/100
final_amount = total + gst_amount
print("------------------------")
print(f"Subtotal: ₹{total}")
print(f"GST @ {gst_rate}%: ₹{gst_amount}")
print(f"Grand Total: ₹{final_amount}")
