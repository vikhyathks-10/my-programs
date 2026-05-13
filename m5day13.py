# 🔹 DAY 13 - ADVANCED REGEX PROJECTS

import re


# 🔹 1. Password Strength Checker

def password_strength(password):

    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1

    if re.search(r'[a-z]', password):
        strength += 1

    if re.search(r'\d', password):
        strength += 1

    if re.search(r'[@$!%*?&]', password):
        strength += 1

    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    return levels.get(strength, "Invalid")


# 🔹 2. Email Extractor from File

def extract_emails(filename):

    with open(filename, "r") as f:
        data = f.read()

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        data
    )

    return emails


# 🔹 3. Log Pattern Analyzer

def analyze_logs(logs):

    error_count = len(re.findall(r'ERROR', logs))
    warning_count = len(re.findall(r'WARNING', logs))
    info_count = len(re.findall(r'INFO', logs))

    return {
        "ERROR": error_count,
        "WARNING": warning_count,
        "INFO": info_count
    }


# 🔹 4. Search & Replace Tool

def search_replace(text, old, new):

    return re.sub(old, new, text)


# 🔹 5. Regex-Based Parser

def parse_data(text):

    names = re.findall(r'Name:\s([A-Za-z ]+)', text)

    ages = re.findall(r'Age:\s(\d+)', text)

    return list(zip(names, ages))


# 🔹 MAIN PROGRAM

print("\n--- Password Strength Checker ---")

print(password_strength("Strong@123"))


print("\n--- Email Extractor ---")

# create sample file
with open("emails.txt", "w") as f:
    f.write("""
    test@gmail.com
    hello@yahoo.com
    admin@company.org
    """)

print(extract_emails("emails.txt"))


print("\n--- Log Pattern Analyzer ---")

logs = """
INFO User logged in
ERROR Database failed
WARNING Disk almost full
ERROR Timeout occurred
"""

print(analyze_logs(logs))


print("\n--- Search & Replace Tool ---")

text = "Python is easy. Python is powerful."

print(search_replace(text, "Python", "Java"))


print("\n--- Regex-Based Parser ---")

sample = """
Name: Vikyat Age: 19
Name: Rahul Age: 21
"""

print(parse_data(sample))