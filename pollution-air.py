aqi = int(input("Enter AQI value: "))

if aqi <= 50:
    category = "Good"
    message = "Air quality is satisfactory."
elif aqi <= 100:
    category = "Moderate"
    message = "Acceptable but some pollutants may be a concern."
elif aqi <= 200:
    category = "Poor"
    message = "Health effects possible for sensitive group."
else:
    category = "Very Poor"
    message = "Everyone may experience health effects."

print("Category:", category)
print("Message :", message)
