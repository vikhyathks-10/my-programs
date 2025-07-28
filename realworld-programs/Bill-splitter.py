total_bill = float(input("Enter the total bill amount: ₹"))
num_people = int(input("Enter number of people to split the bill: "))
tip_percent = float(input("Enter tip percentage (0 if none): "))
tip_amount = (tip_percent / 100) * total_bill
final_amount = total_bill + tip_amount
amount_per_person = final_amount / num_people
print(f"\nEach person should pay: ₹{amount_per_person:.2f}")
