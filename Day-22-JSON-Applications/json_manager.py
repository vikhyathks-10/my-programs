# ============================================================
# MONTH 8 - DAY 22
# JSON APPLICATIONS
#
# Programs 111-115
#
# Concepts:
# JSON, dictionaries, file handling, lists
#
# How to run:
# python json_manager.py
# ============================================================

import json
import os


# ============================================================
# FILE NAMES
# ============================================================

DATA_FILE = "app_data.json"
CONFIG_FILE = "config.json"


# ============================================================
# PROGRAM 111
# CREATE A JSON DATA FILE
# ============================================================

def create_json_file():

    sample_data = {
        "students": [
            {
                "id": "S101",
                "name": "Rahul",
                "course": "CSE",
                "age": 20
            },
            {
                "id": "S102",
                "name": "Priya",
                "course": "ISE",
                "age": 21
            },
            {
                "id": "S103",
                "name": "Arjun",
                "course": "ECE",
                "age": 20
            },
            {
                "id": "S104",
                "name": "Sneha",
                "course": "CSE",
                "age": 21
            }
        ]
    }

    try:

        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                sample_data,
                file,
                indent=4
            )

        print(
            f"\nJSON data file "
            f"'{DATA_FILE}' created successfully."
        )

    except Exception as e:

        print(
            f"\nError creating JSON file: {e}"
        )


# ============================================================
# PROGRAM 112
# READ AND DISPLAY JSON DATA
# ============================================================

def read_json_data():

    if not os.path.exists(DATA_FILE):

        print(
            f"\n'{DATA_FILE}' does not exist."
        )

        print(
            "Please create the JSON file first."
        )

        return None

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        print("\n" + "=" * 55)
        print("              JSON DATA")
        print("=" * 55)

        students = data.get(
            "students",
            []
        )

        if not students:

            print("No student records found.")

        else:

            for student in students:

                print(
                    f"\nID     : {student['id']}"
                )

                print(
                    f"Name   : {student['name']}"
                )

                print(
                    f"Course : {student['course']}"
                )

                print(
                    f"Age    : {student['age']}"
                )

                print("-" * 30)

        return data

    except json.JSONDecodeError:

        print(
            "\nError: Invalid JSON format."
        )

        return None

    except Exception as e:

        print(
            f"\nError reading JSON file: {e}"
        )

        return None


# ============================================================
# PROGRAM 113
# SEARCH RECORDS INSIDE JSON
# ============================================================

def search_json_record():

    data = read_json_data_silently()

    if data is None:

        return

    students = data.get(
        "students",
        []
    )

    if not students:

        print(
            "\nNo student records available."
        )

        return

    search_id = input(
        "\nEnter Student ID to search: "
    ).strip()

    found_student = None

    for student in students:

        if student.get("id") == search_id:

            found_student = student

            break

    if found_student:

        print("\n" + "=" * 45)
        print("             STUDENT FOUND")
        print("=" * 45)

        print(
            f"ID     : {found_student['id']}"
        )

        print(
            f"Name   : {found_student['name']}"
        )

        print(
            f"Course : {found_student['course']}"
        )

        print(
            f"Age    : {found_student['age']}"
        )

        print("=" * 45)

    else:

        print(
            f"\nStudent with ID "
            f"'{search_id}' not found."
        )


# ============================================================
# PROGRAM 114
# UPDATE JSON RECORDS
# ============================================================

def update_json_record():

    data = read_json_data_silently()

    if data is None:

        return

    students = data.get(
        "students",
        []
    )

    if not students:

        print(
            "\nNo student records available."
        )

        return

    student_id = input(
        "\nEnter Student ID to update: "
    ).strip()

    student_to_update = None

    for student in students:

        if student.get("id") == student_id:

            student_to_update = student

            break

    if student_to_update is None:

        print(
            f"\nStudent with ID "
            f"'{student_id}' not found."
        )

        return

    print("\nCurrent Information:")

    print(
        f"Name   : {student_to_update['name']}"
    )

    print(
        f"Course : {student_to_update['course']}"
    )

    print(
        f"Age    : {student_to_update['age']}"
    )

    print(
        "\nPress Enter to keep the current value."
    )

    new_name = input(
        f"Name [{student_to_update['name']}]: "
    ).strip()

    new_course = input(
        f"Course [{student_to_update['course']}]: "
    ).strip()

    new_age = input(
        f"Age [{student_to_update['age']}]: "
    ).strip()

    if new_name:

        student_to_update["name"] = new_name

    if new_course:

        student_to_update["course"] = new_course

    if new_age:

        try:

            age = int(new_age)

            if age > 0:

                student_to_update["age"] = age

            else:

                print(
                    "Invalid age. "
                    "Keeping previous age."
                )

        except ValueError:

            print(
                "Invalid age. "
                "Keeping previous age."
            )

    save_json_data(data)


# ============================================================
# HELPER FUNCTION
# READ JSON WITHOUT DISPLAYING
# ============================================================

def read_json_data_silently():

    if not os.path.exists(DATA_FILE):

        print(
            f"\n'{DATA_FILE}' does not exist."
        )

        print(
            "Choose option 1 first "
            "to create the JSON file."
        )

        return None

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data

    except json.JSONDecodeError:

        print(
            "\nError: Invalid JSON format."
        )

        return None

    except Exception as e:

        print(
            f"\nError reading JSON file: {e}"
        )

        return None


# ============================================================
# HELPER FUNCTION
# SAVE JSON DATA
# ============================================================

def save_json_data(data):

    try:

        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print(
            "\nJSON record updated successfully."
        )

    except Exception as e:

        print(
            f"\nError saving JSON data: {e}"
        )


# ============================================================
# PROGRAM 115
# JSON-BASED CONFIGURATION MANAGER
# ============================================================

def create_default_config():

    default_config = {
        "application": {
            "name": "Student JSON Manager",
            "version": "1.0"
        },
        "settings": {
            "theme": "dark",
            "language": "English",
            "notifications": True
        }
    }

    if not os.path.exists(CONFIG_FILE):

        try:

            with open(
                CONFIG_FILE,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    default_config,
                    file,
                    indent=4
                )

            print(
                f"\nDefault configuration "
                f"'{CONFIG_FILE}' created."
            )

        except Exception as e:

            print(
                f"\nError creating configuration: {e}"
            )


def configuration_manager():

    create_default_config()

    while True:

        print("\n" + "=" * 55)
        print("          JSON CONFIGURATION MANAGER")
        print("=" * 55)

        print("1. View Configuration")
        print("2. Update Application Name")
        print("3. Change Theme")
        print("4. Change Language")
        print("5. Toggle Notifications")
        print("6. Back to Main Menu")

        print("=" * 55)

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # View configuration
        # ----------------------------------------------------

        if choice == "1":

            try:

                with open(
                    CONFIG_FILE,
                    "r",
                    encoding="utf-8"
                ) as file:

                    config = json.load(file)

                print("\n--- Current Configuration ---")

                print(
                    json.dumps(
                        config,
                        indent=4
                    )
                )

            except Exception as e:

                print(
                    f"\nError reading configuration: {e}"
                )

        # ----------------------------------------------------
        # Update application name
        # ----------------------------------------------------

        elif choice == "2":

            new_name = input(
                "Enter new application name: "
            ).strip()

            if new_name:

                update_configuration(
                    "application",
                    "name",
                    new_name
                )

            else:

                print(
                    "\nApplication name cannot be empty."
                )

        # ----------------------------------------------------
        # Change theme
        # ----------------------------------------------------

        elif choice == "3":

            new_theme = input(
                "Enter theme (light/dark): "
            ).strip().lower()

            if new_theme in ["light", "dark"]:

                update_configuration(
                    "settings",
                    "theme",
                    new_theme
                )

            else:

                print(
                    "\nPlease enter either "
                    "'light' or 'dark'."
                )

        # ----------------------------------------------------
        # Change language
        # ----------------------------------------------------

        elif choice == "4":

            new_language = input(
                "Enter language: "
            ).strip()

            if new_language:

                update_configuration(
                    "settings",
                    "language",
                    new_language
                )

            else:

                print(
                    "\nLanguage cannot be empty."
                )

        # ----------------------------------------------------
        # Toggle notifications
        # ----------------------------------------------------

        elif choice == "5":

            toggle_notifications()

        # ----------------------------------------------------
        # Back
        # ----------------------------------------------------

        elif choice == "6":

            break

        else:

            print(
                "\nInvalid choice."
            )


# ============================================================
# UPDATE CONFIGURATION
# ============================================================

def update_configuration(
    section,
    key,
    value
):

    try:

        with open(
            CONFIG_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            config = json.load(file)

        config[section][key] = value

        with open(
            CONFIG_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                config,
                file,
                indent=4
            )

        print(
            "\nConfiguration updated successfully."
        )

    except Exception as e:

        print(
            f"\nError updating configuration: {e}"
        )


# ============================================================
# TOGGLE NOTIFICATIONS
# ============================================================

def toggle_notifications():

    try:

        with open(
            CONFIG_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            config = json.load(file)

        current_value = config[
            "settings"
        ][
            "notifications"
        ]

        config[
            "settings"
        ][
            "notifications"
        ] = not current_value

        with open(
            CONFIG_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                config,
                file,
                indent=4
            )

        print(
            "\nNotifications:",
            not current_value
        )

    except Exception as e:

        print(
            f"\nError updating notifications: {e}"
        )


# ============================================================
# MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 60)
    print("               JSON APPLICATIONS")
    print("=" * 60)

    print("1. Create JSON Data File")
    print("2. Read and Display JSON Data")
    print("3. Search Record in JSON")
    print("4. Update JSON Record")
    print("5. JSON Configuration Manager")
    print("6. Exit")

    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print(
        "\nWelcome to JSON Applications!"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Program 111
        # ----------------------------------------------------

        if choice == "1":

            create_json_file()

        # ----------------------------------------------------
        # Program 112
        # ----------------------------------------------------

        elif choice == "2":

            read_json_data()

        # ----------------------------------------------------
        # Program 113
        # ----------------------------------------------------

        elif choice == "3":

            search_json_record()

        # ----------------------------------------------------
        # Program 114
        # ----------------------------------------------------

        elif choice == "4":

            update_json_record()

        # ----------------------------------------------------
        # Program 115
        # ----------------------------------------------------

        elif choice == "5":

            configuration_manager()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "6":

            print(
                "\nThank you for using "
                "JSON Applications!"
            )

            break

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 6."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()