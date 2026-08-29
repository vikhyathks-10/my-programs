# ============================================================
# MONTH 8 - DAY 29
# LOGGING & DEBUGGING
#
# Programs 146-150
#
# 146. Create a Basic Log File
# 147. Record Program Errors
# 148. Create Different Log Levels
# 149. Add Logging to an Existing Program
# 150. Build a Program Activity Logger
#
# Library:
# logging
#
# How to run:
# python logging_debugging.py
# ============================================================

import logging
from datetime import datetime


LOG_FILE = "program.log"


# ============================================================
# LOGGING CONFIGURATION
# ============================================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)


# ============================================================
# PROGRAM 146
# CREATE A BASIC LOG FILE
# ============================================================

def basic_log_file():

    print("\n" + "=" * 60)
    print("       PROGRAM 146 - BASIC LOG FILE")
    print("=" * 60)

    logger.info(
        "Program 146 started."
    )

    print(
        "\nWriting messages to program.log..."
    )

    logger.debug(
        "Debug message: basic log function started."
    )

    logger.info(
        "Information message: program is running."
    )

    logger.warning(
        "Warning message: this is a sample warning."
    )

    print(
        "\nLog messages written successfully!"
    )

    print(
        f"Check the '{LOG_FILE}' file."
    )

    logger.info(
        "Program 146 completed."
    )


# ============================================================
# PROGRAM 147
# RECORD PROGRAM ERRORS
# ============================================================

def error_logger():

    print("\n" + "=" * 60)
    print("       PROGRAM 147 - ERROR LOGGER")
    print("=" * 60)

    logger.info(
        "Program 147 started."
    )

    print(
        "\nThis program demonstrates exception logging."
    )

    try:

        number = int(
            input(
                "\nEnter a number: "
            )
        )

        divisor = int(
            input(
                "Enter divisor: "
            )
        )

        result = number / divisor

        print(
            f"\nResult = {result}"
        )

        logger.info(
            "Division completed successfully."
        )

    except ValueError as error:

        print(
            "\nInvalid input. Please enter numbers only."
        )

        logger.error(
            f"ValueError occurred: {error}"
        )

    except ZeroDivisionError as error:

        print(
            "\nCannot divide by zero."
        )

        logger.error(
            f"ZeroDivisionError occurred: {error}"
        )

    except Exception as error:

        print(
            "\nAn unexpected error occurred."
        )

        logger.exception(
            "Unexpected error occurred."
        )

    logger.info(
        "Program 147 completed."
    )


# ============================================================
# PROGRAM 148
# DIFFERENT LOG LEVELS
# ============================================================

def log_levels():

    print("\n" + "=" * 60)
    print("       PROGRAM 148 - LOG LEVELS")
    print("=" * 60)

    logger.debug(
        "This is a DEBUG message."
    )

    logger.info(
        "This is an INFO message."
    )

    logger.warning(
        "This is a WARNING message."
    )

    logger.error(
        "This is an ERROR message."
    )

    logger.critical(
        "This is a CRITICAL message."
    )

    print(
        "\nFive different log levels were recorded."
    )

    print(
        f"Check the '{LOG_FILE}' file."
    )


# ============================================================
# PROGRAM 149
# LOGGING IN AN EXISTING PROGRAM
# ============================================================

def student_marks_analyzer():

    print("\n" + "=" * 60)
    print("    PROGRAM 149 - LOGGED MARKS ANALYZER")
    print("=" * 60)

    logger.info(
        "Student marks analyzer started."
    )

    try:

        name = input(
            "\nEnter student name: "
        ).strip()

        if not name:

            logger.warning(
                "Empty student name entered."
            )

            print(
                "Student name cannot be empty."
            )

            return

        marks_input = input(
            "Enter marks: "
        )

        marks = float(
            marks_input
        )

        logger.debug(
            f"Marks entered for {name}: {marks}"
        )

        if marks < 0 or marks > 100:

            logger.warning(
                f"Invalid marks entered: {marks}"
            )

            print(
                "Marks must be between 0 and 100."
            )

            return

        if marks >= 90:

            grade = "A"

        elif marks >= 80:

            grade = "B"

        elif marks >= 70:

            grade = "C"

        elif marks >= 60:

            grade = "D"

        else:

            grade = "F"

        print(
            f"\nStudent : {name}"
        )

        print(
            f"Marks   : {marks}"
        )

        print(
            f"Grade   : {grade}"
        )

        logger.info(
            f"Student analyzed successfully: "
            f"{name}, Grade: {grade}"
        )

    except ValueError as error:

        print(
            "\nInvalid marks entered."
        )

        logger.error(
            f"Invalid marks input: {error}"
        )

    except Exception:

        print(
            "\nUnexpected error occurred."
        )

        logger.exception(
            "Unexpected error in marks analyzer."
        )

    finally:

        logger.info(
            "Student marks analyzer finished."
        )


# ============================================================
# PROGRAM 150
# PROGRAM ACTIVITY LOGGER
# ============================================================

def activity_logger():

    print("\n" + "=" * 60)
    print("       PROGRAM 150 - ACTIVITY LOGGER")
    print("=" * 60)

    logger.info(
        "Activity logger started."
    )

    print(
        "\nEnter activities to record."
    )

    print(
        "Type 'done' when finished."
    )

    while True:

        activity = input(
            "\nEnter activity: "
        ).strip()

        if activity.lower() == "done":

            logger.info(
                "User finished entering activities."
            )

            break

        if not activity:

            logger.warning(
                "User entered an empty activity."
            )

            print(
                "Activity cannot be empty."
            )

            continue

        current_time = datetime.now()

        logger.info(
            f"Activity recorded: "
            f"{activity}"
        )

        print(
            f"Activity recorded at "
            f"{current_time.strftime('%H:%M:%S')}"
        )

    print(
        "\nAll activities have been logged."
    )

    print(
        f"Check the '{LOG_FILE}' file."
    )

    logger.info(
        "Activity logger completed."
    )


# ============================================================
# VIEW LOG FILE
# ============================================================

def view_log_file():

    print("\n" + "=" * 60)
    print("             VIEW LOG FILE")
    print("=" * 60)

    try:

        with open(
            LOG_FILE,
            "r"
        ) as file:

            content = file.read()

        if content:

            print(
                "\n" + content
            )

        else:

            print(
                "\nLog file is empty."
            )

    except FileNotFoundError:

        print(
            "\nLog file does not exist yet."
        )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    logger.info(
        "Logging and Debugging application started."
    )

    while True:

        print("\n" + "=" * 65)
        print("          PYTHON LOGGING & DEBUGGING")
        print("=" * 65)

        print(
            "1. Create Basic Log File"
        )

        print(
            "2. Record Program Errors"
        )

        print(
            "3. Demonstrate Log Levels"
        )

        print(
            "4. Logged Student Marks Analyzer"
        )

        print(
            "5. Program Activity Logger"
        )

        print(
            "6. View Log File"
        )

        print(
            "7. Exit"
        )

        print("=" * 65)

        choice = input(
            "Enter your choice: "
        ).strip()

        logger.debug(
            f"Menu choice selected: {choice}"
        )

        if choice == "1":

            basic_log_file()

        elif choice == "2":

            error_logger()

        elif choice == "3":

            log_levels()

        elif choice == "4":

            student_marks_analyzer()

        elif choice == "5":

            activity_logger()

        elif choice == "6":

            view_log_file()

        elif choice == "7":

            logger.info(
                "Application closed by user."
            )

            print(
                "\nThank you for using "
                "Logging & Debugging!"
            )

            break

        else:

            logger.warning(
                f"Invalid menu choice: {choice}"
            )

            print(
                "\nInvalid choice. Please try again."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()