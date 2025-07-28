temp = float(input("Enter current temperature (°C): "))

if temp < 20:
    print("Wear warm clothes.")
elif 20 <= temp <= 30:
    print("Comfortable weather.")
else:
    print("Stay hydrated.")
