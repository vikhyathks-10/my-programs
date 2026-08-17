# 📄 Text File Analysis Tool

Month 8 – Day 17 | Python Practice Roadmap

A menu-driven **Text File Analysis Tool** built using Python. This project combines file handling, string manipulation, dictionaries, lists, and frequency analysis to analyze text files and extract useful information.

The project implements **Programs 86–90 in a single application**.

## 🚀 Programs Implemented

### 86. Word Counter

Counts the total number of words present in a text file.

### 87. Character Frequency Analyzer

Analyzes the frequency of each character in a text file.

### 88. Most Common Word Finder

Finds the word that appears most frequently in a text file.

### 89. Search a Word in Multiple Files

Searches for a specific word across multiple text files and displays how many times it appears in each file.

### 90. Text-File Statistics Analyzer

Calculates detailed statistics including:

* Number of lines
* Number of words
* Number of characters
* Characters excluding spaces
* Number of sentences
* Number of unique words

## 🛠️ Technologies Used

* **Python**
* **File Handling**
* **String Manipulation**
* **Dictionaries**
* **Lists**
* **Collections Counter**
* **Exception Handling**

## 📁 Project Structure

```text
Day-17-Text-File-Analysis/
│
├── text_file_analysis.py
├── sample1.txt
├── sample2.txt
├── sample3.txt
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-17-Text-File-Analysis
```

### 3. Run the program

```bash
python text_file_analysis.py
```

No external libraries are required because `collections` and the other modules used are part of Python's standard library.

## 🎮 How to Use

After starting the application, a menu will appear:

```text
==================================================
        TEXT FILE ANALYSIS TOOL
==================================================
1. Word Counter
2. Character Frequency Analyzer
3. Most Common Word Finder
4. Search Word in Multiple Files
5. Text-File Statistics Analyzer
6. Run All Analyses
7. Exit
==================================================
```

Enter the corresponding number to perform an analysis.

For example:

```text
Enter your choice: 4
Enter word to search: python
```

The program will search for the word in:

```text
sample1.txt
sample2.txt
sample3.txt
```

## 🔄 Program Flow

```text
Start Program
      ↓
Display Menu
      ↓
Select Analysis
      ↓
Read Text File(s)
      ↓
Process Text
      ↓
Analyze Data
      ↓
Display Results
      ↓
Return to Menu
      ↓
Exit
```

## 🧠 Concepts Practiced

* File opening and closing
* `with open()` syntax
* Reading text files
* `split()`
* `splitlines()`
* String manipulation
* String normalization
* Removing punctuation
* Dictionaries
* `Counter`
* Lists
* Loops
* Functions
* Exception handling
* Multiple-file processing
* Menu-driven programming

## 📊 Example Output

### Word Counter

```text
--- Word Counter ---
File: sample1.txt
Total words: 21
```

### Most Common Word

```text
--- Most Common Word ---
Word: python
Frequency: 3
```

### Multiple File Search

```text
--- Multiple File Word Search ---

sample1.txt: 'python' found 3 time(s)
sample2.txt: 'python' found 2 time(s)
sample3.txt: 'python' found 2 time(s)
```

### Text Statistics

```text
--- Text File Statistics ---
File: sample1.txt
Lines: 3
Words: 21
Characters: ...
Characters without spaces: ...
Sentences: 3
Unique words: ...
```

## 📚 Learning Outcome

Through this project, I learned how to work with text files in Python and extract meaningful information from unstructured text.

I practiced reading files, processing strings, counting word and character frequencies, searching across multiple files, and calculating text statistics.

This project also helped strengthen my understanding of **dictionaries, functions, loops, exception handling, and Python's `Counter` class**.

## 🔮 Future Improvements

* 📊 Add graphical statistics
* 📈 Generate charts for word and character frequencies
* 📂 Allow users to select files dynamically
* 🔎 Support case-sensitive and case-insensitive searches
* 📑 Export analysis results to a report
* 🖥️ Add a Tkinter graphical interface
* 📚 Support larger collections of text files
* ☁️ Add PDF and DOCX text analysis

## 👨‍💻 Project Information

**Month:** 8
**Day:** 17
**Programs:** 86–90
**Project:** Text File Analysis Tool
**Language:** Python
**Type:** Menu-Driven Console Application

## 🏷️ Tags

`#Python` `#FileHandling` `#TextAnalysis` `#StringManipulation` `#Dictionaries` `#PythonProjects` `#Programming` `#GitHub` `#LearningInPublic` `#100DaysOfCode`
