balance = float(input("Enter your account balance: ₹"))
amount = float(input("Enter withdrawal amount: ₹"))
if amount <= 0:
    print("Invalid withdrawal amount.")
elif amount > balance:
    print("Insufficient balance.")
else:
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: ₹{balance:.2f}")
