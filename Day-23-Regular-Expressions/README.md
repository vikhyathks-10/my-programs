# 🔎 Regular Expressions

Month 8 – Day 23 | Python Practice Roadmap

A Python-based **Regular Expression Analyzer** that demonstrates how regular expressions can be used to search, validate, extract, and analyze structured information from text.

The project implements **Programs 116–120 in a single application**.

## 🚀 Programs Implemented

### 116. Email Extractor

Searches a text file and extracts email addresses using a regular expression pattern.

Example:

```text
vikhyath@example.com
support@python.org
admin@gmail.com
```

### 117. Phone Number Validator

Validates Indian phone numbers using regular expressions.

Supported examples include:

```text
9876543210
+91-9876543210
+91 9876543210
```

The program also supports basic Indian landline formats such as:

```text
080-12345678
```

### 118. URL Extractor

Searches the text file and extracts HTTP and HTTPS URLs.

Example:

```text
https://www.python.org
https://github.com
https://www.google.com
```

### 119. Find Dates Inside Text

Searches text for dates in the following formats:

```text
DD-MM-YYYY
DD/MM/YYYY
```

Example:

```text
15-08-2026
23/08/2026
25/12/2026
```

### 120. Large Text File Analyzer

Analyzes a text file using multiple regular expression patterns.

The analyzer extracts:

* Email addresses
* Phone numbers
* URLs
* Dates
* Words
* Numbers
* Character count

It provides a summary of the useful information found inside the text.

## 🛠️ Technologies Used

* **Python**
* **Regular Expressions**
* **`re` module**
* **File Handling**
* **Strings**
* **Pattern Matching**
* **Exception Handling**

## 📁 Project Structure

```text
Day-23-Regular-Expressions/
│
├── regex_analyzer.py
├── sample_text.txt
└── README.md
```

`sample_text.txt` is automatically created when the program runs for the first time.

## ▶️ How to Run

Navigate to the project folder:

```bash
cd Day-23-Regular-Expressions
```

Run the program:

```bash
python regex_analyzer.py
```

No external packages are required.

The `re` module is included in Python's standard library.

## 🎮 Main Menu

The program displays:

```text
============================================================
              REGULAR EXPRESSIONS
============================================================
1. Email Extractor
2. Phone Number Validator
3. URL Extractor
4. Find Dates in Text
5. Large Text File Analyzer
6. Run All Programs
7. Exit
============================================================
```

## 📧 Email Extraction

The application searches the text file using a regular expression:

```python
email_pattern = r"""
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.
    [a-zA-Z]{2,}
"""
```

It extracts all matching email addresses from the text.

## 📱 Phone Validation

The application uses:

```python
phone_pattern = r"^(\+91[- ]?)?[6-9]\d{9}$"
```

This validates common Indian mobile number formats.

Example:

```text
9876543210          → Valid
+91-9876543210     → Valid
+91 8765432109     → Valid
1234567890         → Invalid
98765              → Invalid
```

## 🔗 URL Extraction

The URL pattern used is:

```python
url_pattern = r"https?://[^\s]+"
```

It searches for URLs beginning with:

```text
http://
```

or:

```text
https://
```

## 📅 Date Extraction

The program uses:

```python
date_pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"
```

This can find dates such as:

```text
15-08-2026
23/08/2026
25/12/2026
```

## 📄 Text File Analysis

The analyzer uses multiple patterns to extract useful information from the file.

Example results:

```text
--- TEXT ANALYSIS RESULTS ---

Characters      : ...
Words           : ...
Numbers         : ...
Emails          : ...
Phone Numbers   : ...
URLs            : ...
Dates           : ...
```

## 🔄 Program Flow

```text
Start
  ↓
Create / Read Text File
  ↓
Display Menu
  ↓
Select Regex Operation
  ↓
Apply Regular Expression
  ↓
Find / Validate / Extract Data
  ↓
Display Results
  ↓
Return to Menu
  ↓
Exit
```

## 🧠 Regular Expression Concepts Practiced

### `re.findall()`

Finds all occurrences of a pattern:

```python
re.findall(pattern, text)
```

### `re.fullmatch()`

Checks whether the entire input matches a pattern:

```python
re.fullmatch(pattern, text)
```

### `\d`

Matches a digit.

```text
\d
```

### `\s`

Matches whitespace.

```text
\s
```

### `\b`

Represents a word boundary.

```text
\b
```

### `{n}`

Specifies an exact number of repetitions.

Example:

```text
\d{10}
```

means exactly 10 digits.

### `+`

Means one or more occurrences.

Example:

```text
\d+
```

matches one or more digits.

## 📚 Learning Outcome

Through this project, I learned how regular expressions can be used to identify patterns inside text.

I practiced extracting emails, validating phone numbers, finding URLs, detecting dates, and analyzing a larger text file.

Regular expressions are useful in applications such as:

* Data cleaning
* Form validation
* Log analysis
* Web scraping
* Information extraction
* Text processing
* Data preprocessing

## 🔮 Future Improvements

* 📧 Validate email addresses more strictly
* 📱 Support international phone numbers
* 🌐 Extract domains separately from URLs
* 📅 Validate actual calendar dates
* 📄 Analyze multiple text files
* 🔍 Search custom patterns entered by the user
* 📊 Generate text-analysis reports
* 🧹 Build a text-cleaning tool
* 📝 Add keyword frequency analysis
* 🖥️ Build a Tkinter GUI

## 👨‍💻 Project Information

**Month:** 8
**Day:** 23
**Programs:** 116–120
**Project:** Regular Expression Analyzer
**Language:** Python
**Module:** `re`
**Type:** Text Processing & Pattern Matching

## 🏷️ Tags

`#Python` `#Regex` `#RegularExpressions` `#TextProcessing` `#PatternMatching` `#PythonProjects` `#DataProcessing` `#Programming` `#GitHub` `#LearningInPublic`
