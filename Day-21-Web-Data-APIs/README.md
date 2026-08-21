# 🌐 Web Data & APIs

Month 8 – Day 21 | Python Practice Roadmap

A Python-based **API Information Application** that demonstrates how Python communicates with external web services, fetches data from a public API, processes JSON responses, extracts selected information, and handles API and network errors.

The project implements **Programs 106–110 in a single application**.

## 🚀 Programs Implemented

### 106. Fetch Data from a Public API

Uses Python's `requests` library to send an HTTP GET request to the **REST Countries API** and retrieve country information.

### 107. Parse JSON Response

Converts the API's JSON response into Python data structures using:

```python
response.json()
```

### 108. Extract Selected Fields

Extracts useful information from the JSON response, including:

* Country name
* Official name
* Capital
* Region
* Subregion
* Population
* Area
* Languages
* Currency

### 109. Handle API Errors

Handles different types of problems including:

* Connection errors
* Request timeouts
* Invalid responses
* Country not found
* Bad requests
* Too many requests
* Server errors
* Unexpected API responses

### 110. API-Based Information Program

Combines all the concepts into a simple interactive **Country Information Application**.

The user enters a country name and the application fetches and displays its information from the public API.

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **REST API**
* **JSON**
* **Dictionaries**
* **Lists**
* **Functions**
* **Exception Handling**
* **HTTP Status Codes**

## 🌐 API Used

This project uses the **REST Countries API**.

Base endpoint:

```text
https://restcountries.com/v3.1/name/
```

The API provides information about countries including population, capital, region, languages, and currencies.

No API key is required for this project.

## 📁 Project Structure

```text
Day-21-Web-Data-APIs/
│
├── api_information.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-21-Web-Data-APIs
```

### 3. Install Requests

```bash
pip install requests
```

If `pip` does not work, try:

```bash
python -m pip install requests
```

## ▶️ How to Run

Run the program using:

```bash
python api_information.py
```

The application displays:

```text
============================================================
             WEB DATA & APIs
============================================================
1. Fetch Country Data
2. Parse and Display JSON
3. Extract Selected Fields
4. Test API Error Handling
5. Country Information Program
6. Exit
============================================================
```

## 🎮 How to Use

### Country Information

Select:

```text
5
```

Enter a country:

```text
Enter country name: India
```

The program retrieves the country information from the API and displays the selected fields.

### Example

```text
=======================================================
          COUNTRY INFORMATION
=======================================================
Country       : India
Official Name : Republic of India
Capital       : New Delhi
Region        : Asia
Subregion     : Southern Asia
Population    : ...
Area          : ... km²
Languages     : ...
Currencies    : Indian rupee
=======================================================
```

## 🔄 API Request Flow

```text
User enters country
        ↓
Python creates API URL
        ↓
requests.get()
        ↓
REST Countries API
        ↓
HTTP Response
        ↓
Check Status Code
        ↓
Parse JSON
        ↓
Extract Required Fields
        ↓
Display Information
```

## 📦 JSON Processing

The API returns structured JSON data.

Python converts the response into Python objects:

```python
data = response.json()
```

The application then accesses nested dictionaries and lists to extract the required information.

For example:

```python
country_data["name"]["common"]
```

extracts the common country name.

## ⚠️ Error Handling

The program handles several possible errors.

### Connection Error

```text
Unable to connect to the internet.
```

### Timeout

```text
Request timed out.
```

### 404 Not Found

```text
Country not found.
```

### Server Error

```text
The API may be temporarily unavailable.
```

### Invalid JSON

```text
Response is not valid JSON.
```

## 🧠 Concepts Practiced

* APIs
* HTTP requests
* HTTP GET
* JSON
* `requests.get()`
* `response.status_code`
* `response.json()`
* Dictionaries
* Lists
* Nested data structures
* Functions
* Exception handling
* Network error handling
* API error handling
* Data extraction

## 📚 Learning Outcome

Through this project, I learned how Python communicates with external web services using APIs.

I learned how to send HTTP requests, receive JSON responses, convert JSON data into Python structures, extract specific fields, and handle network and API errors.

This project provides the foundation for building applications that work with **real-time external data and online services**.

## 🔮 Future Improvements

* 🌦️ Add weather information
* 📰 Build a news API application
* 💱 Add currency exchange information
* 🎬 Add movie information using an API
* 📈 Add stock market information
* 🖥️ Build a Tkinter API dashboard
* 💾 Save API results to JSON or CSV
* 🔍 Add advanced search and filtering
* 📊 Visualize API data using Matplotlib

## 👨‍💻 Project Information

**Month:** 8
**Day:** 21
**Programs:** 106–110
**Project:** Web Data & APIs
**Language:** Python
**API:** REST Countries API
**Library:** Requests
**Data Format:** JSON
**Type:** API-Based Information Application

## 🏷️ Tags

`#Python` `#APIs` `#RESTAPI` `#JSON` `#Requests` `#WebData` `#PythonProjects` `#Programming` `#DataAnalysis` `#GitHub` `#LearningInPublic`
