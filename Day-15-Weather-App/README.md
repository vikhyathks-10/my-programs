# 🌦️ Desktop Weather Application

Month 8 – Day 15 | Python Practice Roadmap

A simple desktop Weather Application built using **Python, Tkinter, Requests, JSON, and the OpenWeather API**. The application allows users to search for a city and view its current weather information through a graphical user interface.

## 🚀 Features

* 🔍 Search weather by city name
* 🌡️ Display temperature in Celsius
* 💧 Display humidity
* 💨 Display wind speed
* ☁️ Display weather conditions
* 🌐 Real-time API integration
* 🖥️ User-friendly Tkinter GUI
* ⚠️ Error handling for invalid cities and network problems
* 📦 JSON data processing

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – GUI development
* **Requests** – HTTP/API requests
* **JSON** – Processing API responses
* **OpenWeather API** – Real-time weather data

## 📁 Project Structure

```text
Day-15-Weather-App/
│
├── weather_app.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-15-Weather-App
```

### 3. Install the Requests library

```bash
pip install requests
```

Tkinter is included with most Python installations.

## 🔑 API Key Setup

This project uses the **OpenWeather API**.

1. Create an account on OpenWeather.
2. Generate your API key.
3. Open `weather_app.py`.
4. Replace:

```python
self.api_key = "YOUR_API_KEY"
```

with your API key.

> ⚠️ Do not upload your API key publicly to GitHub.

## ▶️ How to Run

Run the following command:

```bash
python weather_app.py
```

The application window will open.

Enter a city name such as:

```text
Bangalore
```

and click **🔍 Search Weather**.

The application will display:

* 📍 City
* 🌡️ Temperature
* 💧 Humidity
* 💨 Wind Speed
* ☁️ Weather Condition

## 🔄 How It Works

```text
User enters city
        ↓
Tkinter GUI
        ↓
Python sends API request
        ↓
OpenWeather API
        ↓
JSON response
        ↓
Python extracts weather data
        ↓
Tkinter displays weather
```

## 🧠 Python Concepts Practiced

* Object-Oriented Programming
* Classes and Objects
* Functions and Methods
* Tkinter GUI
* API Integration
* HTTP Requests
* JSON Data Handling
* Dictionaries
* Exception Handling
* Event-Driven Programming

## 📚 Learning Outcome

Through this project, I learned how to connect a Python application with a **real-world external API**, send HTTP requests, process JSON responses, handle errors, and display live information through a Tkinter graphical interface.

This project also helped me combine the **Python and OOP concepts learned earlier in the roadmap** with practical API integration.

## 🔮 Future Improvements

* 🌍 Add weather forecast for multiple days
* 🌙 Add dark/light mode
* 🎨 Improve GUI design
* 📍 Add location-based weather detection
* 🌡️ Support Celsius and Fahrenheit
* 🖼️ Display weather icons
* 🔐 Store API keys securely using environment variables

## 👨‍💻 Project Information

**Month:** 8
**Day:** 15
**Project:** Desktop Weather Application
**Language:** Python
**GUI:** Tkinter
**API:** OpenWeather API

## 🏷️ Tags

`#Python` `#WeatherApp` `#Tkinter` `#API` `#OpenWeather` `#JSON` `#OOP` `#PythonProjects` `#Programming` `#GitHub` `#LearningInPublic` `#100DaysOfCode`
