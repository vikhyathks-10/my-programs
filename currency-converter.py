rate = 83 
print("Currency Converter")
print("1. INR to USD")
print("2. USD to INR")

choice = input("Choose option (1 or 2): ")

if choice == "1":
    inr = float(input("Enter amount in INR: ₹"))
    usd = inr / rate
    print(f"₹{inr} = ${usd:.2f}")
elif choice == "2":
    usd = float(input("Enter amount in USD: $"))
    inr = usd * rate
    print(f"${usd} = ₹{inr:.2f}")
else:
    print("Invalid choice.")
