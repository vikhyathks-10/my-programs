# ============================================================
# MONTH 8 - DAY 23
# REGULAR EXPRESSIONS
#
# Programs 116-120
#
# Concepts:
# re, regular expressions, pattern matching,
# strings, file handling
#
# How to run:
# python regex_analyzer.py
# ============================================================

import re
import os


# ============================================================
# FILE CONFIGURATION
# ============================================================

TEXT_FILE = "sample_text.txt"


# ============================================================
# SAMPLE TEXT
# ============================================================

SAMPLE_TEXT = """
Welcome to the Python Regular Expression Analyzer.

Contact information:

Email:
vikhyath@example.com
support@python.org
admin@gmail.com

Phone numbers:
+91-9876543210
+91 8765432109
9876543210
080-12345678

Useful websites:
https://www.python.org
https://github.com
https://www.google.com

Important dates:
15-08-2026
23/08/2026
01-09-2026
25/12/2026

Python is a powerful programming language.
Regular expressions are useful for searching,
extracting and validating text.

The project was created on 23/08/2026.
For support, contact help@example.com.
"""


# ============================================================
# CREATE SAMPLE TEXT FILE
# ============================================================

def create_sample_text_file():

    if os.path.exists(TEXT_FILE):

        return

    try:

        with open(
            TEXT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(SAMPLE_TEXT)

        print(
            f"\n'{TEXT_FILE}' created successfully."
        )

    except Exception as e:

        print(
            f"\nError creating text file: {e}"
        )


# ============================================================
# READ TEXT FILE
# ============================================================

def read_text_file():

    try:

        with open(
            TEXT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except FileNotFoundError:

        print(
            f"\n'{TEXT_FILE}' was not found."
        )

        return None

    except Exception as e:

        print(
            f"\nError reading file: {e}"
        )

        return None


# ============================================================
# PROGRAM 116
# EMAIL EXTRACTOR
# ============================================================

def email_extractor():

    print("\n" + "=" * 60)
    print("                  EMAIL EXTRACTOR")
    print("=" * 60)

    text = read_text_file()

    if text is None:

        return

    email_pattern = r"""
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        \.
        [a-zA-Z]{2,}
    """

    emails = re.findall(
        email_pattern,
        text,
        re.VERBOSE
    )

    if emails:

        print("\nEmail addresses found:")

        for email in emails:

            print(
                f"  {email}"
            )

        print(
            f"\nTotal emails found: {len(emails)}"
        )

    else:

        print(
            "\nNo email addresses found."
        )


# ============================================================
# PROGRAM 117
# PHONE NUMBER VALIDATOR
# ============================================================

def phone_number_validator():

    print("\n" + "=" * 60)
    print("               PHONE NUMBER VALIDATOR")
    print("=" * 60)

    phone = input(
        "\nEnter a phone number: "
    ).strip()

    # Supports:
    # 9876543210
    # +91-9876543210
    # +91 9876543210
    # 080-12345678

    phone_pattern = r"^(\+91[- ]?)?[6-9]\d{9}$"

    if re.fullmatch(
        phone_pattern,
        phone
    ):

        print(
            "\nValid Indian mobile number."
        )

    else:

        # Check landline-style number
        landline_pattern = r"^0\d{2,4}-\d{6,8}$"

        if re.fullmatch(
            landline_pattern,
            phone
        ):

            print(
                "\nValid landline number."
            )

        else:

            print(
                "\nInvalid phone number."
            )


# ============================================================
# PROGRAM 118
# URL EXTRACTOR
# ============================================================

def url_extractor():

    print("\n" + "=" * 60)
    print("                    URL EXTRACTOR")
    print("=" * 60)

    text = read_text_file()

    if text is None:

        return

    url_pattern = r"https?://[^\s]+"

    urls = re.findall(
        url_pattern,
        text
    )

    if urls:

        print("\nURLs found:")

        for url in urls:

            print(
                f"  {url}"
            )

        print(
            f"\nTotal URLs found: {len(urls)}"
        )

    else:

        print(
            "\nNo URLs found."
        )


# ============================================================
# PROGRAM 119
# FIND DATES INSIDE TEXT
# ============================================================

def find_dates():

    print("\n" + "=" * 60)
    print("                  DATE FINDER")
    print("=" * 60)

    text = read_text_file()

    if text is None:

        return

    # Supports:
    # DD-MM-YYYY
    # DD/MM/YYYY

    date_pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"

    dates = re.findall(
        date_pattern,
        text
    )

    if dates:

        print("\nDates found:")

        for date in dates:

            print(
                f"  {date}"
            )

        print(
            f"\nTotal dates found: {len(dates)}"
        )

    else:

        print(
            "\nNo dates found."
        )


# ============================================================
# PROGRAM 120
# LARGE TEXT FILE ANALYZER
# ============================================================

def analyze_large_text_file():

    print("\n" + "=" * 60)
    print("             LARGE TEXT FILE ANALYZER")
    print("=" * 60)

    text = read_text_file()

    if text is None:

        return

    # --------------------------------------------------------
    # Extract emails
    # --------------------------------------------------------

    email_pattern = r"""
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        \.
        [a-zA-Z]{2,}
    """

    emails = re.findall(
        email_pattern,
        text,
        re.VERBOSE
    )

    # --------------------------------------------------------
    # Extract URLs
    # --------------------------------------------------------

    url_pattern = r"https?://[^\s]+"

    urls = re.findall(
        url_pattern,
        text
    )

    # --------------------------------------------------------
    # Extract dates
    # --------------------------------------------------------

    date_pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"

    dates = re.findall(
        date_pattern,
        text
    )

    # --------------------------------------------------------
    # Extract phone numbers
    # --------------------------------------------------------

    phone_pattern = (
        r"(?:\+91[- ]?)?[6-9]\d{9}"
    )

    phone_numbers = re.findall(
        phone_pattern,
        text
    )

    # --------------------------------------------------------
    # Count words
    # --------------------------------------------------------

    words = re.findall(
        r"\b[A-Za-z]+\b",
        text
    )

    # --------------------------------------------------------
    # Count numbers
    # --------------------------------------------------------

    numbers = re.findall(
        r"\b\d+\b",
        text
    )

    # --------------------------------------------------------
    # Display results
    # --------------------------------------------------------

    print("\n--- TEXT ANALYSIS RESULTS ---")

    print(
        f"Characters      : {len(text)}"
    )

    print(
        f"Words           : {len(words)}"
    )

    print(
        f"Numbers         : {len(numbers)}"
    )

    print(
        f"Emails          : {len(emails)}"
    )

    print(
        f"Phone Numbers   : {len(phone_numbers)}"
    )

    print(
        f"URLs            : {len(urls)}"
    )

    print(
        f"Dates           : {len(dates)}"
    )

    # --------------------------------------------------------
    # Display extracted information
    # --------------------------------------------------------

    print("\nEmails:")

    if emails:

        for email in emails:

            print(
                f"  {email}"
            )

    else:

        print("  None")

    print("\nURLs:")

    if urls:

        for url in urls:

            print(
                f"  {url}"
            )

    else:

        print("  None")

    print("\nDates:")

    if dates:

        for date in dates:

            print(
                f"  {date}"
            )

    else:

        print("  None")

    print("\nPhone Numbers:")

    if phone_numbers:

        for phone in phone_numbers:

            print(
                f"  {phone}"
            )

    else:

        print("  None")


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 60)
    print("              REGULAR EXPRESSIONS")
    print("=" * 60)

    print("1. Email Extractor")
    print("2. Phone Number Validator")
    print("3. URL Extractor")
    print("4. Find Dates in Text")
    print("5. Large Text File Analyzer")
    print("6. Run All Programs")
    print("7. Exit")

    print("=" * 60)


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs():

    print(
        "\nRunning Programs 116-120..."
    )

    email_extractor()

    url_extractor()

    find_dates()

    analyze_large_text_file()

    print(
        "\nPhone Number Validation"
    )

    test_numbers = [
        "9876543210",
        "+91-9876543210",
        "+91 8765432109",
        "1234567890",
        "98765"
    ]

    for phone in test_numbers:

        phone_pattern = r"^(\+91[- ]?)?[6-9]\d{9}$"

        if re.fullmatch(
            phone_pattern,
            phone
        ):

            result = "Valid"

        else:

            result = "Invalid"

        print(
            f"{phone:<20} : {result}"
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    create_sample_text_file()

    print(
        "\nWelcome to Regular Expressions!"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Program 116
        # ----------------------------------------------------

        if choice == "1":

            email_extractor()

        # ----------------------------------------------------
        # Program 117
        # ----------------------------------------------------

        elif choice == "2":

            phone_number_validator()

        # ----------------------------------------------------
        # Program 118
        # ----------------------------------------------------

        elif choice == "3":

            url_extractor()

        # ----------------------------------------------------
        # Program 119
        # ----------------------------------------------------

        elif choice == "4":

            find_dates()

        # ----------------------------------------------------
        # Program 120
        # ----------------------------------------------------

        elif choice == "5":

            analyze_large_text_file()

        # ----------------------------------------------------
        # Run all
        # ----------------------------------------------------

        elif choice == "6":

            run_all_programs()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "7":

            print(
                "\nThank you for using "
                "Regular Expressions!"
            )

            break

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 7."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()