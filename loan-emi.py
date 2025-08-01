P = float(input("Enter loan amount (Principal): "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan term (in years): "))

R = annual_rate / (12 * 100)  
N = years * 12  

emi = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)

print(f"Your monthly EMI is: ₹{emi:.2f}")

