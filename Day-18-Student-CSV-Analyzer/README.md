# 📊 Student CSV Analyzer

Month 8 – Day 18 | Python Practice Roadmap

A menu-driven **Student CSV Analyzer** built using Python. This project reads student marks from a CSV file, calculates averages, identifies the highest-scoring student, filters students based on their marks, and generates a summary CSV file.

The project implements **Programs 91–95 in a single application**.

## 🚀 Programs Implemented

### 91. Read Student CSV

Reads student records from `students.csv` using Python's `csv.DictReader`.

### 92. Calculate Average Marks

Calculates the average marks of each student across:

* Python
* C++
* DBMS
* Maths

### 93. Find Highest-Scoring Student

Calculates the average of every student and identifies the student with the highest average score.

### 94. Filter Students Above a Particular Mark

Allows the user to enter a minimum average mark and displays students whose average is equal to or greater than that value.

### 95. Generate a Summary CSV

Creates a new `summary.csv` file containing:

* Student name
* Average marks
* Grade

## 🛠️ Technologies Used

* **Python**
* **CSV Module**
* **Lists**
* **Dictionaries**
* **File Handling**
* **Functions**
* **Loops**
* **Conditional Statements**
* **Exception Handling**

## 📁 Project Structure

```text
Day-18-Student-CSV-Analyzer/
│
├── student_csv_analyzer.py
├── students.csv
├── summary.csv
└── README.md
```

## 📄 Input CSV Format

The `students.csv` file contains student names and marks:

```csv
Name,Python,C++,DBMS,Maths
Rahul,85,78,90,88
Priya,92,89,95,91
Arjun,76,82,79,85
Sneha,88,94,91,89
Vikhyath,95,91,93,96
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-18-Student-CSV-Analyzer
```

### 3. Run the application

```bash
python student_csv_analyzer.py
```

No external libraries are required because Python's built-in `csv` module is used.

## 🎮 How to Use

After starting the application, the following menu appears:

```text
=======================================================
           STUDENT CSV ANALYZER
=======================================================
1. Read Student CSV
2. Calculate Average Marks
3. Find Highest-Scoring Student
4. Filter Students Above a Mark
5. Generate Summary CSV
6. Run All Programs
7. Exit
=======================================================
```

Enter the corresponding number to perform an operation.

## 📊 Example

### Average Marks

```text
--- Average Marks ---

Rahul: 85.25
Priya: 91.75
Arjun: 80.50
Sneha: 90.50
Vikhyath: 93.75
```

### Highest-Scoring Student

```text
--- Highest-Scoring Student ---

Student: Vikhyath
Average: 93.75
```

### Filtering Students

If the user enters:

```text
Enter minimum average mark: 90
```

The application displays:

```text
--- Students With Average Above 90 ---

Priya -> 91.75
Sneha -> 90.50
Vikhyath -> 93.75
```

## 📄 Generated Summary CSV

The application creates `summary.csv`:

```csv
Name,Average,Grade
Rahul,85.25,A
Priya,91.75,A+
Arjun,80.50,A
Sneha,90.50,A+
Vikhyath,93.75,A+
```

## 🧮 Average Calculation

The average is calculated using:

```text
Average = (Python + C++ + DBMS + Maths) / 4
```

## 🏆 Grading System

|  Average | Grade |
| -------: | :---- |
|   90–100 | A+    |
| 80–89.99 | A     |
| 70–79.99 | B     |
| 60–69.99 | C     |
| 50–59.99 | D     |
| Below 50 | F     |

## 🔄 Program Flow

```text
Start
  ↓
Read students.csv
  ↓
Display Menu
  ↓
Choose Operation
  ↓
Process Student Data
  ↓
Display Results
  ↓
Generate summary.csv if required
  ↓
Return to Menu
  ↓
Exit
```

## 🧠 Concepts Practiced

* CSV file reading
* CSV file writing
* `csv.DictReader`
* `csv.DictWriter`
* Lists
* Dictionaries
* File handling
* Functions
* Loops
* Conditional statements
* Exception handling
* Data filtering
* Average calculation
* Data summarization

## 📚 Learning Outcome

Through this project, I learned how to work with **structured data stored in CSV files** using Python.

I practiced reading records into dictionaries, performing calculations on student marks, comparing and filtering records, and writing processed data into a new CSV file.

This project provides a foundation for working with larger datasets and prepares for future Python data-analysis projects.

## 🔮 Future Improvements

* 📊 Add graphical charts for student performance
* 📈 Add subject-wise analysis
* 🏆 Display top 3 students
* 📉 Find lowest-scoring student
* 🔎 Search for a particular student
* ✏️ Add and update student records
* 📂 Allow users to select CSV files
* 🖥️ Build a Tkinter GUI
* 📑 Export a detailed student report

## 👨‍💻 Project Information

**Month:** 8
**Day:** 18
**Programs:** 91–95
**Project:** Student CSV Analyzer
**Language:** Python
**Data Format:** CSV
**Type:** Menu-Driven Console Application

## 🏷️ Tags

`#Python` `#CSV` `#FileHandling` `#DataAnalysis` `#PythonProjects` `#Dictionaries` `#Lists` `#Programming` `#GitHub` `#LearningInPublic`
