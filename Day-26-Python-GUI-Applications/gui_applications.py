# ============================================================
# MONTH 8 - DAY 26
# PYTHON GUI APPLICATIONS
#
# Programs 131-135
#
# 131. Basic Calculator GUI
# 132. To-Do List GUI
# 133. Unit Converter GUI
# 134. Student Marks Calculator GUI
# 135. Mini Login System GUI
#
# Library:
# tkinter
#
# How to run:
# python gui_applications.py
# ============================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# ============================================================
# PROGRAM 131
# BASIC CALCULATOR GUI
# ============================================================

def calculator_gui():

    window = tk.Toplevel()

    window.title(
        "Basic Calculator"
    )

    window.geometry(
        "350x450"
    )

    window.resizable(
        False,
        False
    )

    # --------------------------------------------------------
    # Variables
    # --------------------------------------------------------

    expression = tk.StringVar()

    # --------------------------------------------------------
    # Display
    # --------------------------------------------------------

    display = tk.Entry(
        window,
        textvariable=expression,
        font=("Arial", 22),
        justify="right",
        bd=5,
        relief="sunken"
    )

    display.pack(
        padx=15,
        pady=20,
        fill="x"
    )

    # --------------------------------------------------------
    # Button Functions
    # --------------------------------------------------------

    def add_value(value):

        expression.set(
            expression.get() + str(value)
        )

    def clear():

        expression.set("")

    def calculate():

        try:

            result = eval(
                expression.get()
            )

            expression.set(
                str(result)
            )

        except Exception:

            messagebox.showerror(
                "Calculator Error",
                "Invalid expression."
            )

            expression.set("")

    # --------------------------------------------------------
    # Button Frame
    # --------------------------------------------------------

    button_frame = tk.Frame(
        window
    )

    button_frame.pack(
        padx=10,
        pady=10
    )

    buttons = [
        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("/", 0, 3),

        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("*", 1, 3),

        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("-", 2, 3),

        ("0", 3, 0),
        (".", 3, 1),
        ("+", 3, 2),
        ("=", 3, 3)
    ]

    for text, row, column in buttons:

        if text == "=":

            command = calculate

        else:

            command = lambda value=text: add_value(
                value
            )

        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 16),
            width=5,
            height=2,
            command=command
        )

        button.grid(
            row=row,
            column=column,
            padx=4,
            pady=4
        )

    # --------------------------------------------------------
    # Clear Button
    # --------------------------------------------------------

    clear_button = tk.Button(
        window,
        text="CLEAR",
        font=("Arial", 14),
        width=20,
        command=clear
    )

    clear_button.pack(
        pady=10
    )


# ============================================================
# PROGRAM 132
# TO-DO LIST GUI
# ============================================================

def todo_gui():

    window = tk.Toplevel()

    window.title(
        "To-Do List"
    )

    window.geometry(
        "450x500"
    )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    title = tk.Label(
        window,
        text="To-Do List",
        font=("Arial", 24, "bold")
    )

    title.pack(
        pady=15
    )

    # --------------------------------------------------------
    # Input
    # --------------------------------------------------------

    task_entry = tk.Entry(
        window,
        font=("Arial", 14),
        width=30
    )

    task_entry.pack(
        pady=10
    )

    # --------------------------------------------------------
    # Listbox
    # --------------------------------------------------------

    task_list = tk.Listbox(
        window,
        font=("Arial", 13),
        width=40,
        height=15
    )

    task_list.pack(
        pady=10
    )

    # --------------------------------------------------------
    # Functions
    # --------------------------------------------------------

    def add_task():

        task = task_entry.get().strip()

        if not task:

            messagebox.showwarning(
                "Input Error",
                "Please enter a task."
            )

            return

        task_list.insert(
            tk.END,
            "[ ] " + task
        )

        task_entry.delete(
            0,
            tk.END
        )

    def delete_task():

        selected = task_list.curselection()

        if not selected:

            messagebox.showwarning(
                "Selection",
                "Please select a task."
            )

            return

        task_list.delete(
            selected[0]
        )

    def complete_task():

        selected = task_list.curselection()

        if not selected:

            messagebox.showwarning(
                "Selection",
                "Please select a task."
            )

            return

        index = selected[0]

        task = task_list.get(
            index
        )

        if task.startswith("[ ]"):

            task = task.replace(
                "[ ]",
                "[✓]",
                1
            )

            task_list.delete(
                index
            )

            task_list.insert(
                index,
                task
            )

        else:

            messagebox.showinfo(
                "Task Status",
                "Task is already completed."
            )

    # --------------------------------------------------------
    # Buttons
    # --------------------------------------------------------

    button_frame = tk.Frame(
        window
    )

    button_frame.pack(
        pady=10
    )

    tk.Button(
        button_frame,
        text="Add Task",
        width=12,
        command=add_task
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    tk.Button(
        button_frame,
        text="Complete",
        width=12,
        command=complete_task
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    tk.Button(
        button_frame,
        text="Delete",
        width=12,
        command=delete_task
    ).grid(
        row=0,
        column=2,
        padx=5
    )


# ============================================================
# PROGRAM 133
# UNIT CONVERTER GUI
# ============================================================

def unit_converter_gui():

    window = tk.Toplevel()

    window.title(
        "Unit Converter"
    )

    window.geometry(
        "450x450"
    )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Unit Converter",
        font=("Arial", 24, "bold")
    ).pack(
        pady=20
    )

    # --------------------------------------------------------
    # Conversion Type
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Select Conversion:",
        font=("Arial", 13)
    ).pack(
        pady=5
    )

    conversion_type = ttk.Combobox(
        window,
        values=[
            "Length",
            "Weight",
            "Temperature"
        ],
        state="readonly",
        width=25
    )

    conversion_type.current(
        0
    )

    conversion_type.pack(
        pady=10
    )

    # --------------------------------------------------------
    # Input
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Enter Value:",
        font=("Arial", 13)
    ).pack(
        pady=5
    )

    value_entry = tk.Entry(
        window,
        font=("Arial", 14),
        width=20
    )

    value_entry.pack(
        pady=5
    )

    # --------------------------------------------------------
    # Unit
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Select Unit:",
        font=("Arial", 13)
    ).pack(
        pady=5
    )

    unit_combo = ttk.Combobox(
        window,
        values=[
            "Kilometers to Miles",
            "Miles to Kilometers",
            "Kilograms to Pounds",
            "Pounds to Kilograms",
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius"
        ],
        state="readonly",
        width=25
    )

    unit_combo.current(
        0
    )

    unit_combo.pack(
        pady=10
    )

    # --------------------------------------------------------
    # Result
    # --------------------------------------------------------

    result_label = tk.Label(
        window,
        text="Result: --",
        font=("Arial", 16, "bold")
    )

    result_label.pack(
        pady=20
    )

    # --------------------------------------------------------
    # Convert Function
    # --------------------------------------------------------

    def convert():

        try:

            value = float(
                value_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Input Error",
                "Please enter a valid number."
            )

            return

        conversion = unit_combo.get()

        if conversion == "Kilometers to Miles":

            result = value * 0.621371

            unit = "miles"

        elif conversion == "Miles to Kilometers":

            result = value * 1.60934

            unit = "kilometers"

        elif conversion == "Kilograms to Pounds":

            result = value * 2.20462

            unit = "pounds"

        elif conversion == "Pounds to Kilograms":

            result = value * 0.453592

            unit = "kilograms"

        elif conversion == "Celsius to Fahrenheit":

            result = (
                value * 9 / 5
            ) + 32

            unit = "°F"

        elif conversion == "Fahrenheit to Celsius":

            result = (
                value - 32
            ) * 5 / 9

            unit = "°C"

        else:

            return

        result_label.config(
            text=f"Result: {result:.2f} {unit}"
        )

    # --------------------------------------------------------
    # Convert Button
    # --------------------------------------------------------

    tk.Button(
        window,
        text="Convert",
        font=("Arial", 14),
        width=15,
        command=convert
    ).pack(
        pady=10
    )


# ============================================================
# PROGRAM 134
# STUDENT MARKS CALCULATOR GUI
# ============================================================

def student_marks_gui():

    window = tk.Toplevel()

    window.title(
        "Student Marks Calculator"
    )

    window.geometry(
        "500x600"
    )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Student Marks Calculator",
        font=("Arial", 22, "bold")
    ).pack(
        pady=20
    )

    # --------------------------------------------------------
    # Subject Frame
    # --------------------------------------------------------

    subject_frame = tk.Frame(
        window
    )

    subject_frame.pack(
        pady=10
    )

    subjects = [
        "Python",
        "Data Structures",
        "Database",
        "Computer Networks",
        "Mathematics"
    ]

    entries = []

    for index, subject in enumerate(
        subjects
    ):

        tk.Label(
            subject_frame,
            text=subject,
            font=("Arial", 12),
            width=20,
            anchor="w"
        ).grid(
            row=index,
            column=0,
            padx=10,
            pady=8
        )

        entry = tk.Entry(
            subject_frame,
            font=("Arial", 12),
            width=15
        )

        entry.grid(
            row=index,
            column=1,
            padx=10,
            pady=8
        )

        entries.append(
            entry
        )

    # --------------------------------------------------------
    # Result Labels
    # --------------------------------------------------------

    result_label = tk.Label(
        window,
        text="Total: --\nAverage: --\nGrade: --",
        font=("Arial", 16, "bold"),
        justify="left"
    )

    result_label.pack(
        pady=20
    )

    # --------------------------------------------------------
    # Calculate Function
    # --------------------------------------------------------

    def calculate_marks():

        marks = []

        for entry in entries:

            try:

                mark = float(
                    entry.get()
                )

                if mark < 0 or mark > 100:

                    messagebox.showerror(
                        "Invalid Marks",
                        "Marks must be between 0 and 100."
                    )

                    return

                marks.append(
                    mark
                )

            except ValueError:

                messagebox.showerror(
                    "Input Error",
                    "Please enter valid marks "
                    "for all subjects."
                )

                return

        total = sum(
            marks
        )

        average = total / len(
            marks
        )

        # ----------------------------------------------------
        # Grade
        # ----------------------------------------------------

        if average >= 90:

            grade = "A+"

        elif average >= 80:

            grade = "A"

        elif average >= 70:

            grade = "B"

        elif average >= 60:

            grade = "C"

        elif average >= 50:

            grade = "D"

        else:

            grade = "F"

        result_label.config(
            text=(
                f"Total: {total:.2f}\n"
                f"Average: {average:.2f}\n"
                f"Grade: {grade}"
            )
        )

    # --------------------------------------------------------
    # Reset Function
    # --------------------------------------------------------

    def reset():

        for entry in entries:

            entry.delete(
                0,
                tk.END
            )

        result_label.config(
            text="Total: --\nAverage: --\nGrade: --"
        )

    # --------------------------------------------------------
    # Buttons
    # --------------------------------------------------------

    tk.Button(
        window,
        text="Calculate",
        font=("Arial", 13),
        width=15,
        command=calculate_marks
    ).pack(
        pady=5
    )

    tk.Button(
        window,
        text="Reset",
        font=("Arial", 13),
        width=15,
        command=reset
    ).pack(
        pady=5
    )


# ============================================================
# PROGRAM 135
# MINI LOGIN SYSTEM GUI
# ============================================================

def login_gui():

    window = tk.Toplevel()

    window.title(
        "Mini Login System"
    )

    window.geometry(
        "400x350"
    )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Login System",
        font=("Arial", 24, "bold")
    ).pack(
        pady=25
    )

    # --------------------------------------------------------
    # Username
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Username",
        font=("Arial", 13)
    ).pack(
        pady=5
    )

    username_entry = tk.Entry(
        window,
        font=("Arial", 13),
        width=25
    )

    username_entry.pack(
        pady=5
    )

    # --------------------------------------------------------
    # Password
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Password",
        font=("Arial", 13)
    ).pack(
        pady=5
    )

    password_entry = tk.Entry(
        window,
        font=("Arial", 13),
        width=25,
        show="*"
    )

    password_entry.pack(
        pady=5
    )

    # --------------------------------------------------------
    # Login Function
    # --------------------------------------------------------

    def login():

        username = username_entry.get().strip()

        password = password_entry.get()

        # Demo credentials

        correct_username = "admin"

        correct_password = "python123"

        if not username or not password:

            messagebox.showwarning(
                "Login",
                "Please enter username and password."
            )

            return

        if (
            username == correct_username
            and password == correct_password
        ):

            messagebox.showinfo(
                "Login Successful",
                "Welcome! Login successful."
            )

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

    # --------------------------------------------------------
    # Reset Function
    # --------------------------------------------------------

    def reset():

        username_entry.delete(
            0,
            tk.END
        )

        password_entry.delete(
            0,
            tk.END
        )

    # --------------------------------------------------------
    # Buttons
    # --------------------------------------------------------

    button_frame = tk.Frame(
        window
    )

    button_frame.pack(
        pady=20
    )

    tk.Button(
        button_frame,
        text="Login",
        font=("Arial", 12),
        width=12,
        command=login
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    tk.Button(
        button_frame,
        text="Reset",
        font=("Arial", 12),
        width=12,
        command=reset
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    # --------------------------------------------------------
    # Demo Credentials
    # --------------------------------------------------------

    tk.Label(
        window,
        text=(
            "Demo Username: admin\n"
            "Demo Password: python123"
        ),
        font=("Arial", 10)
    ).pack(
        pady=10
    )


# ============================================================
# MAIN MENU WINDOW
# ============================================================

def main():

    root = tk.Tk()

    root.title(
        "Python GUI Applications"
    )

    root.geometry(
        "500x600"
    )

    root.resizable(
        False,
        False
    )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    title = tk.Label(
        root,
        text="Python GUI Applications",
        font=("Arial", 24, "bold")
    )

    title.pack(
        pady=25
    )

    subtitle = tk.Label(
        root,
        text="Month 8 - Day 26",
        font=("Arial", 14)
    )

    subtitle.pack(
        pady=5
    )

    # --------------------------------------------------------
    # Program Buttons
    # --------------------------------------------------------

    button_frame = tk.Frame(
        root
    )

    button_frame.pack(
        pady=25
    )

    programs = [
        (
            "131. Basic Calculator",
            calculator_gui
        ),
        (
            "132. To-Do List",
            todo_gui
        ),
        (
            "133. Unit Converter",
            unit_converter_gui
        ),
        (
            "134. Student Marks Calculator",
            student_marks_gui
        ),
        (
            "135. Mini Login System",
            login_gui
        )
    ]

    for index, (
        text,
        command
    ) in enumerate(
        programs
    ):

        tk.Button(
            button_frame,
            text=text,
            font=("Arial", 13),
            width=30,
            height=2,
            command=command
        ).pack(
            pady=7
        )

    # --------------------------------------------------------
    # Exit Button
    # --------------------------------------------------------

    tk.Button(
        root,
        text="Exit",
        font=("Arial", 13),
        width=20,
        command=root.destroy
    ).pack(
        pady=15
    )

    # --------------------------------------------------------
    # Start GUI
    # --------------------------------------------------------

    root.mainloop()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()