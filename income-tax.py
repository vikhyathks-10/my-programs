def calculate_tax(income):
    tax = 0

    if income <= 150000:
        tax = 0
    elif income <= 500000:
        tax = (income - 150000) * 0.05
    elif income <= 1000000:
        tax = (150000 * 0.05) + (income - 500000) * 0.20
    else:
        tax = (150000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

    return tax
try:
    income = float(input("Enter your annual income in ₹: "))
    tax = calculate_tax(income)
    print(f"\nEstimated Income Tax Payable: ₹{tax:.2f}")
except ValueError:
    print("❌ Invalid input. Please enter a number.")
