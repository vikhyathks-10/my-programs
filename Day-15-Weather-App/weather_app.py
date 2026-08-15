import tkinter as tk
from tkinter import messagebox
import requests


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Application")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # OpenWeather API Key
        self.api_key="YOUR_NEW_API_KEY"  # Replace with your actual API key
        # Title
        title = tk.Label(
            root,
            text="🌦️ Weather Application",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        # City label
        city_label = tk.Label(
            root,
            text="Enter City Name:",
            font=("Arial", 14)
        )
        city_label.pack(pady=5)

        # City input
        self.city_entry = tk.Entry(
            root,
            font=("Arial", 16),
            width=25,
            justify="center"
        )
        self.city_entry.pack(pady=10)

        # Search button
        search_button = tk.Button(
            root,
            text="🔍 Search Weather",
            font=("Arial", 13, "bold"),
            command=self.get_weather
        )
        search_button.pack(pady=15)

        # Weather information
        self.temperature_label = tk.Label(
            root,
            text="🌡️ Temperature: --",
            font=("Arial", 15)
        )
        self.temperature_label.pack(pady=8)

        self.humidity_label = tk.Label(
            root,
            text="💧 Humidity: --",
            font=("Arial", 15)
        )
        self.humidity_label.pack(pady=8)

        self.wind_label = tk.Label(
            root,
            text="💨 Wind Speed: --",
            font=("Arial", 15)
        )
        self.wind_label.pack(pady=8)

        self.condition_label = tk.Label(
            root,
            text="☁️ Condition: --",
            font=("Arial", 15)
        )
        self.condition_label.pack(pady=8)

        self.city_result_label = tk.Label(
            root,
            text="📍 City: --",
            font=("Arial", 15, "bold")
        )
        self.city_result_label.pack(pady=15)

    def get_weather(self):
        city = self.city_entry.get().strip()

        if not city:
            messagebox.showwarning(
                "Input Error",
                "Please enter a city name."
            )
            return

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 404:
                messagebox.showerror(
                    "Error",
                    "City not found. Please enter a valid city."
                )
                return

            response.raise_for_status()

            data = response.json()

            # Extract data from JSON
            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            condition = data["weather"][0]["description"]

            # Update GUI
            self.city_result_label.config(
                text=f"📍 City: {city_name}"
            )

            self.temperature_label.config(
                text=f"🌡️ Temperature: {temperature} °C"
            )

            self.humidity_label.config(
                text=f"💧 Humidity: {humidity}%"
            )

            self.wind_label.config(
                text=f"💨 Wind Speed: {wind_speed} m/s"
            )

            self.condition_label.config(
                text=f"☁️ Condition: {condition.title()}"
            )

        except requests.exceptions.ConnectionError:
            messagebox.showerror(
                "Connection Error",
                "Unable to connect to the internet."
            )

        except requests.exceptions.Timeout:
            messagebox.showerror(
                "Timeout Error",
                "The request took too long."
            )

        except requests.exceptions.RequestException as e:
            messagebox.showerror(
                "API Error",
                f"Something went wrong:\n{e}"
            )

        except KeyError:
            messagebox.showerror(
                "Data Error",
                "Unexpected data received from the API."
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An unexpected error occurred:\n{e}"
            )


# Create application
root = tk.Tk()

app = WeatherApp(root)

root.mainloop()