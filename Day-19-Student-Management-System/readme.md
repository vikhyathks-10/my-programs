# 🎓 Student Management System

Month 8 – Day 19 | Python Practice Roadmap

A menu-driven **Student Management System** built using Python. The application allows users to add, search, update, delete, and display student records. Student data is stored permanently in a JSON file.

This project implements **Programs 96–100 in a single application**.

## 🚀 Programs Implemented

### 96. Add Student

Allows the user to create a new student record using a unique Student ID.

The system stores:

* Student ID
* Student Name
* Age
* Course
* Email

### 97. Search Student

Searches for a student using their unique Student ID and displays their complete information.

### 98. Update Student

Allows the user to update existing student information while keeping unchanged fields intact.

### 99. Delete Student

Deletes a student record after asking the user for confirmation.

### 100. Complete Menu-Driven Student System

Combines all operations into one interactive menu-driven application.

## 🛠️ Technologies Used

* **Python**
* **Functions**
* **Dictionaries**
* **JSON**
* **File Handling**
* **Loops**
* **Conditional Statements**
* **Exception Handling**
* **CRUD Operations**

## 📁 Project Structure

```text
Day-19-Student-Management-System/
│
├── student_management.py
├── students.json
└── README.md
```

## 📄 Student Data Format

Student records are stored in `students.json`.

Example:

```json
{
    "S101": {
        "name": "Rahul",
        "age": 20,
        "course": "CSE",
        "email": "rahul@gmail.com"
    }
}
```

The `students.json` file can initially contain:

```json
{}
```

The Python program automatically updates the file whenever a student is added, updated, or deleted.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-19-Student-Management-System
```

### 3. Run the application

```bash
python student_management.py
```

No external libraries are required because JSON and file handling use Python's standard library.

## 🎮 How to Use

After starting the application, the following menu appears:

```text
=======================================================
          STUDENT MANAGEMENT SYSTEM
=======================================================
1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display All Students
6. Exit
=======================================================
```

Enter the corresponding number to perform an operation.

## ➕ Adding a Student

Select:

```text
1
```

Example:

```text
Enter Student ID: S101
Enter Student Name: Rahul
Enter Age: 20
Enter Course: CSE
Enter Email: rahul@gmail.com
```

The record is automatically saved to `students.json`.

## 🔍 Searching a Student

Select:

```text
2
```

Enter the Student ID:

```text
Enter Student ID: S101
```

Example output:

```text
Student Found!
------------------------------
ID     : S101
Name   : Rahul
Age    : 20
Course : CSE
Email  : rahul@gmail.com
```

## ✏️ Updating a Student

Select:

```text
3
```

Enter the Student ID and provide the new information.

Pressing **Enter** without entering a new value keeps the existing information.

## 🗑️ Deleting a Student

Select:

```text
4
```

The application asks for confirmation before deleting the record:

```text
Are you sure you want to delete this student? (y/n):
```

The record is removed from `students.json` only after confirmation.

## 👥 Displaying All Students

Select:

```text
5
```

The application displays all currently stored student records.

## 🔄 CRUD Operations

This project demonstrates the four fundamental **CRUD operations**:

| CRUD Operation | Application Feature      |
| -------------- | ------------------------ |
| **Create**     | Add Student              |
| **Read**       | Search / Display Student |
| **Update**     | Update Student           |
| **Delete**     | Delete Student           |

## 🔄 Program Flow

```text
Start Application
       ↓
Load students.json
       ↓
Display Menu
       ↓
Select Operation
       ↓
Add / Search / Update / Delete
       ↓
Save Changes to JSON
       ↓
Return to Menu
       ↓
Exit
```

## 🧠 Concepts Practiced

* Functions
* Dictionaries
* JSON data
* File reading
* File writing
* `json.load()`
* `json.dump()`
* Loops
* Conditional statements
* Input validation
* Exception handling
* CRUD operations
* Menu-driven programming
* Persistent data storage

## 📚 Learning Outcome

Through this project, I learned how to build a basic **data management system** using Python.

I practiced storing structured information using dictionaries, saving data permanently in a JSON file, and implementing Create, Read, Update, and Delete operations.

This project also strengthened my understanding of functions, file handling, user input, validation, and menu-driven application design.

## 🔮 Future Improvements

* 🖥️ Add a Tkinter GUI
* 🔎 Search students by name or course
* 📊 Add student marks and grades
* 📈 Generate performance reports
* 🔐 Add user login and authentication
* 📧 Add email validation
* 📱 Create a web-based version
* 🗄️ Replace JSON with SQLite/MySQL
* 📋 Add sorting and filtering
* 📤 Export student records to CSV

## 👨‍💻 Project Information

**Month:** 8
**Day:** 19
**Programs:** 96–100
**Project:** Student Management System
**Language:** Python
**Data Storage:** JSON
**Type:** Menu-Driven CRUD Application

## 🏷️ Tags

`#Python` `#StudentManagementSystem` `#JSON` `#FileHandling` `#CRUD` `#Dictionaries` `#PythonProjects` `#Programming` `#GitHub` `#LearningInPublic`
