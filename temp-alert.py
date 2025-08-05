temperature = float(input("Enter current temperature (°C): "))

if temperature > 40:
    print("🔥 Alert: It’s too hot outside!")
elif temperature < 10:
    print("❄️ Alert: It’s too cold outside!")
else:
    print("✅ Temperature is normal.")
