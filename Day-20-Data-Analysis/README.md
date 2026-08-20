# 📊 Data Analysis with Python

Month 8 – Day 20 | Python Practice Roadmap

A menu-driven **Student Class Performance Analyzer** built using Python. This project takes raw student marks and converts them into useful information through statistical calculations, sorting, comparison, and grade analysis.

The project implements **Programs 101–105 in a single application**.

## 🚀 Programs Implemented

### 101. Student Marks Statistics

Analyzes the overall student marks and calculates:

* Number of students
* Total marks
* Average marks
* Highest mark
* Lowest mark
* Sorted marks

### 102. Mean, Median and Mode

Calculates the three basic statistical measures:

* Mean
* Median
* Mode

Python's built-in `statistics` module is used for the calculations.

### 103. Highest / Lowest Value Analysis

Identifies:

* Highest mark
* Student(s) with the highest mark
* Lowest mark
* Student(s) with the lowest mark

The program also handles cases where multiple students have the same highest or lowest score.

### 104. Grade Distribution

Assigns grades based on student marks and generates a class-wide grade distribution.

|    Marks | Grade |
| -------: | :---- |
|   90–100 | A+    |
|    80–89 | A     |
|    70–79 | B     |
|    60–69 | C     |
|    50–59 | D     |
| Below 50 | F     |

### 105. Class Performance Analyzer

Combines multiple analysis techniques to provide an overall view of class performance.

It calculates:

* Total students
* Class average
* Highest mark
* Lowest mark
* Number of passed students
* Number of failed students
* Pass percentage
* Students above class average
* Students below class average

## 🛠️ Technologies Used

* **Python**
* **Lists**
* **Dictionaries**
* **Statistics**
* **Sorting**
* **Functions**
* **Loops**
* **Conditional Statements**
* **List Comprehension**
* **Exception Handling**

## 📁 Project Structure

```text
Day-20-Data-Analysis/
│
├── data_analysis.py
└── README.md
```

No external data file is required. The sample student data is stored inside `data_analysis.py`.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-20-Data-Analysis
```

### 3. Run the program

```bash
python data_analysis.py
```

No external packages need to be installed because the project uses Python's standard library.

## 🎮 How to Use

After starting the application, the following menu appears:

```text
=======================================================
          DATA ANALYSIS WITH PYTHON
=======================================================
1. Student Marks Statistics
2. Mean, Median and Mode
3. Highest / Lowest Analysis
4. Grade Distribution
5. Class Performance Analyzer
6. Display Student Data
7. Run All Analyses
8. Exit
=======================================================
```

Enter the corresponding number to perform an analysis.

### Run Everything

To execute all five programs together, select:

```text
7
```

This runs Programs **101–105** sequentially.

## 📊 Sample Student Data

The program uses the following sample data:

```text
Rahul       : 85
Priya       : 92
Arjun       : 76
Sneha       : 88
Vikhyath    : 95
Kiran       : 72
Ananya      : 90
Rohan       : 81
Meera       : 95
Aditya      : 68
```

## 📈 Example Output

### Student Marks Statistics

```text
Number of students : 10
Total marks        : 842
Average marks      : 84.20
Highest mark       : 95
Lowest mark        : 68
```

### Mean, Median and Mode

```text
Mean   : 84.20
Median : 86.50
Mode   : 95
```

### Highest / Lowest Analysis

```text
Highest mark : 95

Student(s) with highest mark:
  Vikhyath
  Meera

Lowest mark : 68

Student(s) with lowest mark:
  Aditya
```

### Grade Distribution

```text
Grade A+: 3 student(s)
Grade A: 3 student(s)
Grade B: 3 student(s)
Grade C: 1 student(s)
Grade D: 0 student(s)
Grade F: 0 student(s)
```

## 🧮 Statistical Concepts

### Mean

The mean represents the average value:

```text
Mean = Sum of all marks / Number of students
```

### Median

The median is the middle value after the data is arranged in sorted order.

### Mode

The mode is the value that occurs most frequently.

## 🔄 Program Flow

```text
Start
  ↓
Load Student Data
  ↓
Display Menu
  ↓
Select Analysis
  ↓
Process Student Marks
  ↓
Calculate Statistics
  ↓
Display Results
  ↓
Return to Menu
  ↓
Exit
```

## 🧠 Concepts Practiced

* Lists
* Dictionaries
* Dictionary values
* `sum()`
* `min()`
* `max()`
* `len()`
* `sorted()`
* Mean calculation
* Median calculation
* Mode calculation
* List comprehension
* Functions
* Loops
* Conditional statements
* Data classification
* Statistical analysis

## 📚 Learning Outcome

Through this project, I learned how to turn **raw student marks into useful information** using Python.

I practiced statistical calculations, sorting, filtering, classification, and comparison of data. I also learned how dictionaries can represent real-world records and how lists can be used to perform numerical analysis.

This project provides a foundation for more advanced **data analysis and data science concepts**.

## 🔮 Future Improvements

* 📊 Add graphical charts using Matplotlib
* 📈 Add subject-wise performance analysis
* 📉 Generate performance trends
* 📄 Read student data from CSV files
* 💾 Export analysis results to CSV
* 🖥️ Build a Tkinter dashboard
* 📊 Create interactive visualizations
* 🔎 Add student search and filtering
* 🏆 Generate a ranked student list

## 👨‍💻 Project Information

**Month:** 8
**Day:** 20
**Programs:** 101–105
**Project:** Data Analysis with Python
**Language:** Python
**Type:** Menu-Driven Data Analysis Application

## 🏷️ Tags

`#Python` `#DataAnalysis` `#Statistics` `#PythonProjects` `#Lists` `#Dictionaries` `#DataScience` `#Programming` `#GitHub` `#LearningInPublic`
