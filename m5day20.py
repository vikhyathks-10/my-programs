# 🔹 DAY 20 - FILE & TEXT AUTOMATION

import os
from collections import Counter


# 🔹 1. Text File Analyzer

def text_file_analyzer(filename):

    print("\n--- Text File Analyzer ---")

    with open(filename, "r") as file:

        content = file.read()

    lines = content.splitlines()
    words = content.split()
    chars = len(content)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", chars)


# 🔹 2. Word Counter

def word_counter(filename):

    print("\n--- Word Counter ---")

    with open(filename, "r") as file:

        content = file.read().lower()

    words = content.split()

    freq = Counter(words)

    for word, count in freq.items():
        print(word, "->", count)


# 🔹 3. Character Frequency Tool

def char_frequency(filename):

    print("\n--- Character Frequency Tool ---")

    with open(filename, "r") as file:

        content = file.read()

    freq = Counter(content)

    for char, count in freq.items():

        if char != "\n":
            print(repr(char), "->", count)


# 🔹 4. PDF Filename Organizer

def pdf_organizer(path):

    print("\n--- PDF Filename Organizer ---")

    pdf_folder = os.path.join(path, "PDF_Files")

    if not os.path.exists(pdf_folder):
        os.mkdir(pdf_folder)

    for file in os.listdir(path):

        if file.endswith(".pdf"):

            old_path = os.path.join(path, file)
            new_path = os.path.join(pdf_folder, file)

            os.rename(old_path, new_path)

            print(file, "moved")


# 🔹 5. Batch Text Replacer

def batch_replace(filename, old_word, new_word):

    print("\n--- Batch Text Replacer ---")

    with open(filename, "r") as file:

        content = file.read()

    updated = content.replace(old_word, new_word)

    with open(filename, "w") as file:

        file.write(updated)

    print("Replacement Completed")


# 🔹 MAIN PROGRAM

# Create sample text file
with open("sample.txt", "w") as f:

    f.write("""
Python is powerful.
Python is easy to learn.
Automation using Python is fun.
""")


text_file_analyzer("sample.txt")

word_counter("sample.txt")

char_frequency("sample.txt")

batch_replace("sample.txt", "Python", "Java")


# ⚠️ Uncomment if testing with PDF files
# pdf_organizer(".")