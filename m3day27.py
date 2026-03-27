filename = "textfile.txt"

while True:

    print("\n------ TEXT UTILITY TOOL ------")
    print("1 Count Words")
    print("2 Remove Spaces")
    print("3 Reverse Content")
    print("4 Convert to Uppercase")
    print("5 Search Word")
    print("6 Exit")

    choice = input("Enter choice: ")

    # 1 Count Words
    if choice == "1":
        try:
            with open(filename, "r") as f:
                text = f.read()
                words = text.split()
                print("Word Count:", len(words))
        except FileNotFoundError:
            print("File not found.")

    # 2 Remove Spaces
    elif choice == "2":
        try:
            with open(filename, "r") as f:
                text = f.read()

            new_text = text.replace(" ", "")

            with open("no_spaces.txt", "w") as f:
                f.write(new_text)

            print("Spaces removed. Saved in no_spaces.txt")

        except FileNotFoundError:
            print("File not found.")

    # 3 Reverse Content
    elif choice == "3":
        try:
            with open(filename, "r") as f:
                text = f.read()

            reversed_text = text[::-1]

            with open("reversed.txt", "w") as f:
                f.write(reversed_text)

            print("Reversed content saved in reversed.txt")

        except FileNotFoundError:
            print("File not found.")

    # 4 Uppercase File
    elif choice == "4":
        try:
            with open(filename, "r") as f:
                text = f.read()

            upper_text = text.upper()

            with open("uppercase.txt", "w") as f:
                f.write(upper_text)

            print("Uppercase content saved in uppercase.txt")

        except FileNotFoundError:
            print("File not found.")

    # 5 Search Word
    elif choice == "5":
        word = input("Enter word to search: ")

        try:
            with open(filename, "r") as f:
                text = f.read()

            if word.lower() in text.lower():
                print("Word found in file.")
            else:
                print("Word not found.")

        except FileNotFoundError:
            print("File not found.")

    # Exit
    elif choice == "6":
        break

    else:
        print("Invalid choice")