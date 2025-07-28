height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
else:
    category = "Overweight"
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
