# m3day20.py
# DAY 20 — File Handling + Exception Handling

import shutil
import os

# -------------------------------
# 1. Safe File Copier
# -------------------------------
def safe_copy():
    try:
        src = input("Enter source file: ")
        dest = input("Enter destination file: ")

        if not os.path.exists(src):
            raise FileNotFoundError("Source file does not exist")

        shutil.copy(src, dest)
        print("File copied successfully!")

    except Exception as e:
        print("Error:", e)


# -------------------------------
# 2. File Search with Error Handling
# -------------------------------
def file_search():
    try:
        filename = input("Enter file name: ")
        word = input("Enter word to search: ")

        with open(filename, "r") as file:
            content = file.read()

        if word in content:
            print(f"'{word}' found in file!")
        else:
            print(f"'{word}' not found.")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# -------------------------------
# 3. Count Words with File Safety
# -------------------------------
def count_words():
    try:
        filename = input("Enter file name: ")

        with open(filename, "r") as file:
            words = file.read().split()

        print("Total words:", len(words))

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# -------------------------------
# 4. Replace Word with Exception Handling
# -------------------------------
def replace_word():
    try:
        filename = input("Enter file name: ")
        old_word = input("Enter word to replace: ")
        new_word = input("Enter new word: ")

        with open(filename, "r") as file:
            content = file.read()

        if old_word not in content:
            raise ValueError("Word not found in file")

        content = content.replace(old_word, new_word)

        with open(filename, "w") as file:
            file.write(content)

        print("Word replaced successfully!")

    except FileNotFoundError:
        print("File not found!")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Error:", e)


# -------------------------------
# 5. File Backup System
# -------------------------------
def backup_file():
    try:
        filename = input("Enter file to backup: ")

        if not os.path.exists(filename):
            raise FileNotFoundError("File does not exist")

        backup_name = filename + ".bak"

        shutil.copy(filename, backup_name)
        print(f"Backup created: {backup_name}")

    except Exception as e:
        print("Error:", e)


# -------------------------------
# MENU SYSTEM
# -------------------------------
def main():
    while True:
        print("\n===== DAY 20 MENU =====")
        print("1. Safe File Copier")
        print("2. File Search")
        print("3. Count Words")
        print("4. Replace Word")
        print("5. Backup File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            safe_copy()
        elif choice == "2":
            file_search()
        elif choice == "3":
            count_words()
        elif choice == "4":
            replace_word()
        elif choice == "5":
            backup_file()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
if __name__ == "__main__":
    main()