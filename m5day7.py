# 🔹 DAY 7 - MIXED LIBRARY PRACTICE

import os
import random
import time
from collections import Counter


# 🔹 1. File Organizer

def file_organizer():
    print("\n--- File Organizer ---")

    files = os.listdir()

    for file in files:
        if os.path.isfile(file):

            ext = file.split(".")[-1] if "." in file else "others"

            folder_name = ext.upper() + "_Files"

            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            source = file
            destination = os.path.join(folder_name, file)

            # Avoid moving current python file accidentally
            if file != os.path.basename(__file__):
                os.rename(source, destination)

    print("Files Organized")


# 🔹 2. Random Quiz Generator

def random_quiz():
    print("\n--- Random Quiz Generator ---")

    questions = {
        "Capital of India?": "Delhi",
        "2 + 2 = ?": "4",
        "Python is interpreted?": "yes"
    }

    question = random.choice(list(questions.keys()))

    answer = input(question + " : ")

    if answer.lower() == questions[question].lower():
        print("Correct!")
    else:
        print("Wrong Answer")


# 🔹 3. Execution Timer Tool

def execution_timer():
    print("\n--- Execution Timer ---")

    start = time.time()

    total = 0
    for i in range(1000000):
        total += i

    end = time.time()

    print("Execution Time:",
          round(end - start, 4), "seconds")


# 🔹 4. Mini Command-Line Utility

def command_line_utility():
    print("\n--- Mini Command Utility ---")

    print("Current Directory:")
    print(os.getcwd())

    print("\nFiles:")
    for file in os.listdir():
        print(file)


# 🔹 5. Folder Statistics Analyzer

def folder_statistics():
    print("\n--- Folder Statistics ---")

    files = os.listdir()

    extensions = []

    for file in files:
        if os.path.isfile(file) and "." in file:
            ext = file.split(".")[-1]
            extensions.append(ext)

    stats = Counter(extensions)

    print("File Type Counts:")

    for ext, count in stats.items():
        print(ext, "->", count)


# 🔹 MAIN PROGRAM

print("\n====== DAY 7 PROJECTS ======")

# ⚠️ Uncomment organizer only if needed
# file_organizer()

random_quiz()

execution_timer()

command_line_utility()

folder_statistics()