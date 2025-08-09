aqi = int(input("Enter the AQI (Air Quality Index) value: "))
if 0 <= aqi <= 50:
    category = "Good"
    message = "Air quality is satisfactory, and air pollution poses little or no risk."
elif 51 <= aqi <= 100:
    category = "Moderate"
    message = "Air quality is acceptable. Some pollutants may cause minor health issues."
elif 101 <= aqi <= 200:
    category = "Poor"
    message = "Air quality is unhealthy for sensitive groups. Limit outdoor activities."
else:
    category = "Very Poor or Hazardous"
    message = "Air quality is very unhealthy or hazardous. Avoid outdoor exposure!"

print(f"\nAQI: {aqi}")
print(f"Category: {category}")
print(f"Health Message: {message}")
