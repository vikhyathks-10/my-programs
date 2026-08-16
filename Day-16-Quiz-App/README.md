# 🧠 Python Quiz Application

Month 8 – Day 16 | Python Practice Roadmap

A desktop-based **Python Quiz Application** built using **Python, Tkinter, JSON, and Object-Oriented Programming**. The application presents multiple-choice questions, checks the user's answers, keeps track of the score, and displays the final result.

## 🚀 Features

* 🧠 Multiple-choice Python questions
* 🔘 Interactive radio-button options
* ✅ Automatic answer checking
* 📊 Real-time score tracking
* ➡️ Next question navigation
* 🏆 Final score and percentage
* 🔄 Restart quiz option
* 📄 Questions stored in a JSON file
* ⚠️ Error handling for missing or invalid JSON files
* 🖥️ User-friendly Tkinter GUI

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – GUI development
* **JSON** – Question storage and data management
* **Object-Oriented Programming** – Application structure
* **File Handling** – Reading quiz questions

## 📁 Project Structure

```text
Day-16-Quiz-App/
│
├── quiz_app.py
├── questions.json
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-16-Quiz-App
```

### 3. Run the application

```bash
python quiz_app.py
```

No external Python libraries are required because Tkinter and JSON are part of the standard Python installation.

## 🎮 How to Use

1. Launch the application.
2. Read the displayed question.
3. Select one of the four options.
4. Click **Submit Answer**.
5. The application will indicate whether the answer is correct.
6. Continue to the next question.
7. After completing all questions, your final score and percentage will be displayed.
8. Click **Restart Quiz** to play again.

## 📊 Scoring System

The application calculates the percentage using:

```text
Percentage = (Correct Answers / Total Questions) × 100
```

For example:

```text
Score: 8/10
Percentage: 80.0%
```

## 🔄 How It Works

```text
Start Application
        ↓
Load questions.json
        ↓
Display Question
        ↓
User Selects Answer
        ↓
Submit Answer
        ↓
Check Correct Answer
        ↓
Update Score
        ↓
Next Question
        ↓
All Questions Completed?
        ↓
Display Final Result
        ↓
Restart / Exit
```

## 🧠 Python Concepts Practiced

* Classes and Objects
* Object-Oriented Programming
* Tkinter GUI
* JSON File Handling
* Lists and Dictionaries
* Functions and Methods
* Exception Handling
* `StringVar`
* Event-Driven Programming
* Conditional Statements
* Score Calculation
* File Reading

## 📚 Learning Outcome

Through this project, I learned how to build an interactive desktop application using **Tkinter and Object-Oriented Programming**.

I also learned how to store structured data in a **JSON file**, read that data using Python, handle user input, validate answers, maintain application state, and calculate the final score.

This project helped me combine the Python concepts learned throughout the roadmap into a practical GUI-based application.

## 🔮 Future Improvements

* ⏱️ Add a timer for each question
* 🏅 Add difficulty levels
* 📚 Add different quiz categories
* 📈 Add a detailed score dashboard
* 💾 Store previous scores
* 🔀 Randomize questions and options
* 🎨 Improve the GUI design
* 🔊 Add sound effects
* 🌐 Create an online question database

## 👨‍💻 Project Information

Month: 8
Day:16
Project: Python Quiz Application
Language:Python
GUI:Tkinter
Data Format: JSON
Concepts: OOP, File Handling, Exception Handling

## 🏷️ Tags

`#Python` `#QuizApp` `#Tkinter` `#JSON` `#OOP` `#PythonProjects` `#Programming` `#GitHub` `#LearningInPublic` `#100DaysOfCode`
