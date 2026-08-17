from collections import Counter
import os
import string


# --------------------------------------------------
# PROGRAM 86
# Word Counter
# --------------------------------------------------

def word_counter(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()

        print("\n--- Word Counter ---")
        print(f"File: {filename}")
        print(f"Total words: {len(words)}")

    except FileNotFoundError:
        print("File not found.")


# --------------------------------------------------
# PROGRAM 87
# Character Frequency Analyzer
# --------------------------------------------------

def character_frequency(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        frequency = Counter(
            char.lower()
            for char in text
            if not char.isspace()
        )

        print("\n--- Character Frequency Analyzer ---")

        for character, count in frequency.most_common():
            print(f"{repr(character)} : {count}")

    except FileNotFoundError:
        print("File not found.")


# --------------------------------------------------
# PROGRAM 88
# Most Common Word Finder
# --------------------------------------------------

def most_common_word(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        # Remove punctuation
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        words = text.split()

        if not words:
            print("The file contains no words.")
            return

        frequency = Counter(words)

        word, count = frequency.most_common(1)[0]

        print("\n--- Most Common Word ---")
        print(f"Word: {word}")
        print(f"Frequency: {count}")

    except FileNotFoundError:
        print("File not found.")


# --------------------------------------------------
# PROGRAM 89
# Search a Word in Multiple Files
# --------------------------------------------------

def search_word_multiple_files(filenames, search_word):

    print("\n--- Multiple File Word Search ---")

    search_word = search_word.lower()

    found = False

    for filename in filenames:

        try:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read().lower()

            words = text.translate(
                str.maketrans("", "", string.punctuation)
            ).split()

            count = words.count(search_word)

            if count > 0:
                print(
                    f"{filename}: "
                    f"'{search_word}' found {count} time(s)"
                )
                found = True
            else:
                print(
                    f"{filename}: "
                    f"'{search_word}' not found"
                )

        except FileNotFoundError:
            print(f"{filename}: File not found.")

    if not found:
        print(
            f"\n'{search_word}' was not found "
            "in any file."
        )


# --------------------------------------------------
# PROGRAM 90
# Text-File Statistics Analyzer
# --------------------------------------------------

def text_statistics(filename):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()

        characters = len(text)

        characters_without_spaces = sum(
            1 for char in text
            if not char.isspace()
        )

        lines = text.splitlines()

        sentences = sum(
            text.count(symbol)
            for symbol in ".!?"
        )

        unique_words = len(
            set(
                word.lower().strip(string.punctuation)
                for word in words
                if word.strip(string.punctuation)
            )
        )

        print("\n--- Text File Statistics ---")
        print(f"File: {filename}")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {characters}")
        print(
            f"Characters without spaces: "
            f"{characters_without_spaces}"
        )
        print(f"Sentences: {sentences}")
        print(f"Unique words: {unique_words}")

    except FileNotFoundError:
        print("File not found.")


# --------------------------------------------------
# DISPLAY MENU
# --------------------------------------------------

def display_menu():

    print("\n" + "=" * 50)
    print("        TEXT FILE ANALYSIS TOOL")
    print("=" * 50)

    print("1. Word Counter")
    print("2. Character Frequency Analyzer")
    print("3. Most Common Word Finder")
    print("4. Search Word in Multiple Files")
    print("5. Text-File Statistics Analyzer")
    print("6. Run All Analyses")
    print("7. Exit")

    print("=" * 50)


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

def main():

    filename = "sample1.txt"

    multiple_files = [
        "sample1.txt",
        "sample2.txt",
        "sample3.txt"
    ]

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            word_counter(filename)

        elif choice == "2":

            character_frequency(filename)

        elif choice == "3":

            most_common_word(filename)

        elif choice == "4":

            search_word = input(
                "Enter word to search: "
            ).strip()

            if search_word:
                search_word_multiple_files(
                    multiple_files,
                    search_word
                )
            else:
                print("Please enter a word.")

        elif choice == "5":

            text_statistics(filename)

        elif choice == "6":

            print("\nRunning all analyses...")

            word_counter(filename)

            character_frequency(filename)

            most_common_word(filename)

            search_word = input(
                "\nEnter a word to search "
                "in all files: "
            ).strip()

            if search_word:
                search_word_multiple_files(
                    multiple_files,
                    search_word
                )

            text_statistics(filename)

        elif choice == "7":

            print("\nThank you for using Text File Analysis Tool!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()