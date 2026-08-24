# 🌐 Web Scraping Basics

Month 8 – Day 24 | Python Practice Roadmap

A Python-based **Webpage Information Extractor** that demonstrates the basics of collecting structured information from HTML webpages using `requests` and BeautifulSoup.

The project implements **Programs 121–125 in a single menu-driven application**.

## 🚀 Programs Implemented

### 121. Extract Page Title

Fetches a webpage and extracts the content inside the HTML `<title>` tag.

Example:

```html
<title>Welcome to Python.org</title>
```

The program extracts:

```text
Welcome to Python.org
```

### 122. Extract All Headings

Finds headings from:

* `<h1>`
* `<h2>`
* `<h3>`
* `<h4>`
* `<h5>`
* `<h6>`

and displays their text and heading level.

### 123. Extract Links

Finds all `<a>` elements and extracts their `href` attributes.

Relative URLs are converted into complete URLs using `urljoin()`.

Example:

```text
/about/
```

can become:

```text
https://www.python.org/about/
```

### 124. Extract Structured Information

Collects basic webpage information including:

* Page title
* Meta description
* Number of headings
* Number of links
* Number of images
* Number of paragraphs
* Main headings

### 125. Basic Webpage Information Extractor

Combines the previous concepts into a complete webpage analyzer.

The extractor displays:

* URL
* Page title
* Headings
* Links
* Paragraphs
* Images
* Meta description

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **BeautifulSoup**
* **HTML**
* **Web Scraping**
* **URL Processing**
* **Exception Handling**

## 📦 Required Libraries

This project requires:

```text
requests
beautifulsoup4
```

Install them using:

```bash
python -m pip install requests beautifulsoup4
```

## 📁 Project Structure

```text
Day-24-Web-Scraping-Basics/
│
├── web_scraper.py
└── README.md
```

No input file is required.

The program retrieves webpage HTML directly from the internet.

## ▶️ How to Run

Navigate to the project folder:

```bash
cd Day-24-Web-Scraping-Basics
```

Install the required packages:

```bash
python -m pip install requests beautifulsoup4
```

Run the program:

```bash
python web_scraper.py
```

## 🌐 Default Website

The default website used for testing is:

```text
https://www.python.org
```

When prompted for a URL, pressing Enter uses the default website.

You can also enter another publicly accessible webpage, for example:

```text
https://example.com
```

## 🎮 Main Menu

The application displays:

```text
=================================================================
               WEB SCRAPING BASICS
=================================================================
1. Extract Page Title
2. Extract All Headings
3. Extract Links
4. Extract Structured Information
5. Webpage Information Extractor
6. Run All Programs
7. Exit
=================================================================
```

## 🏷️ HTML Elements Used

### Title

```html
<title>Page Title</title>
```

Python:

```python
soup.find("title")
```

### Headings

```html
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
```

Python:

```python
soup.find_all(["h1", "h2"])
```

### Links

```html
<a href="https://example.com">
    Example
</a>
```

Python:

```python
link.get("href")
```

### Images

```html
<img src="image.jpg">
```

Python:

```python
soup.find_all("img")
```

### Paragraphs

```html
<p>This is a paragraph.</p>
```

Python:

```python
soup.find_all("p")
```

## 🔄 Web Scraping Flow

```text
Start
  ↓
Enter Website URL
  ↓
Send HTTP Request
  ↓
Receive HTML
  ↓
Create BeautifulSoup Object
  ↓
Find HTML Elements
  ↓
Extract Information
  ↓
Display Results
  ↓
Return to Menu
  ↓
Exit
```

## 🧠 Concepts Practiced

* HTML structure
* HTTP requests
* `requests.get()`
* HTTP status codes
* BeautifulSoup
* `BeautifulSoup()`
* `find()`
* `find_all()`
* `get()`
* `get_text()`
* HTML tags
* HTML attributes
* URL handling
* `urljoin()`
* Exception handling

## 📚 Learning Outcome

Through this project, I learned the fundamentals of web scraping using Python.

I learned how to request a webpage, receive HTML content, parse the HTML using BeautifulSoup, locate specific HTML elements, and extract useful structured information.

These concepts form the foundation for more advanced tasks such as:

* Web data collection
* Data extraction
* Web research automation
* Dataset creation
* Price monitoring
* News collection
* Website analysis

## ⚠️ Responsible Web Scraping

When scraping websites, always respect:

* Website terms of service
* `robots.txt`
* Rate limits
* Server resources
* Copyright restrictions
* Privacy requirements

Avoid sending excessive requests to websites.

## 🔮 Future Improvements

* 📊 Save scraped data to CSV
* 💾 Save results to JSON
* 📰 Build a news scraper
* 🛒 Build a product-price tracker
* 🔎 Search specific HTML elements
* 📈 Analyze scraped data
* 🖥️ Build a Tkinter scraping dashboard
* 🔄 Add scheduled scraping
* 📂 Scrape multiple webpages
* 🧹 Clean and process scraped text

## 👨‍💻 Project Information

**Month:** 8
**Day:** 24
**Programs:** 121–125
**Project:** Web Scraping Basics
**Language:** Python
**Libraries:** Requests, BeautifulSoup
**Data Format:** HTML
**Type:** Web Data Extraction

## 🏷️ Tags

`#Python` `#WebScraping` `#BeautifulSoup` `#Requests` `#HTML` `#WebData` `#PythonProjects` `#DataExtraction` `#Programming` `#GitHub` `#LearningInPublic`
