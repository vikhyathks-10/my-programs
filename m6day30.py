# 🔹 DAY 30 - PYTHON FLUENCY TEST

import csv
import os


# ==========================================
# Utility
# ==========================================

class Utility:

    @staticmethod
    def header(title):

        print("\n" + "=" * 50)

        print(title)

        print("=" * 50)


# ==========================================
# 1. ARRAY CHALLENGE
# Find Largest Element
# ==========================================

def array_challenge():

    Utility.header("ARRAY CHALLENGE")

    numbers = list(map(int,
                       input("Enter Numbers : ").split()))

    print("Largest Element :", max(numbers))

    print("Smallest Element :", min(numbers))

    print("Sum :", sum(numbers))


# ==========================================
# 2. STRING CHALLENGE
# ==========================================

def string_challenge():

    Utility.header("STRING CHALLENGE")

    text = input("Enter String : ")

    print("Reverse :", text[::-1])

    print("Palindrome :", text == text[::-1])

    vowels = "aeiouAEIOU"

    count = sum(
        1 for ch in text
        if ch in vowels
    )

    print("Vowels :", count)


# ==========================================
# 3. DSA CHALLENGE
# Binary Search
# ==========================================

def binary_search():

    Utility.header("DSA CHALLENGE")

    numbers = list(map(int,
                       input("Sorted Numbers : ").split()))

    target = int(input("Target : "))

    left = 0

    right = len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:

            print("Found At Index", mid)

            return

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    print("Element Not Found")


# ==========================================
# 4. PROJECT CHALLENGE
# Mini Contact Book
# ==========================================

FILE_NAME = "contacts.csv"


def load_contacts():

    contacts = []

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME,
                  "r",
                  newline="") as file:

            contacts = list(csv.reader(file))

    return contacts


def save_contacts(data):

    with open(FILE_NAME,
              "w",
              newline="") as file:

        writer = csv.writer(file)

        writer.writerows(data)


def project_challenge():

    while True:

        Utility.header("CONTACT BOOK")

        print("1. Add Contact")

        print("2. View Contacts")

        print("3. Back")

        choice = input("Choice : ")

        if choice == "1":

            contacts = load_contacts()

            name = input("Name : ")

            phone = input("Phone : ")

            contacts.append([name, phone])

            save_contacts(contacts)

            print("Contact Saved")

        elif choice == "2":

            contacts = load_contacts()

            if not contacts:

                print("No Contacts")

            else:

                for contact in contacts:

                    print(contact[0], "-", contact[1])

        elif choice == "3":

            break

        else:

            print("Invalid Choice")


# ==========================================
# 5. OPTIMIZATION CHALLENGE
# Two Sum (Hash Map)
# ==========================================

def optimization_challenge():

    Utility.header("OPTIMIZATION CHALLENGE")

    numbers = list(map(int,
                       input("Numbers : ").split()))

    target = int(input("Target : "))

    hashmap = {}

    for index, value in enumerate(numbers):

        difference = target - value

        if difference in hashmap:

            print("Pair Found :")

            print(hashmap[difference], index)

            return

        hashmap[value] = index

    print("No Pair Found")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    Utility.header("DAY 30 - PYTHON FLUENCY TEST 🚀")

    print("1. Array Challenge")

    print("2. String Challenge")

    print("3. DSA Challenge")

    print("4. Project Challenge")

    print("5. Optimization Challenge")

    print("6. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        array_challenge()

    elif choice == "2":

        string_challenge()

    elif choice == "3":

        binary_search()

    elif choice == "4":

        project_challenge()

    elif choice == "5":

        optimization_challenge()

    elif choice == "6":

        print("\n🎉 Congratulations!")

        print("You Successfully Completed Month 6 🚀")

        break

    else:

        print("Invalid Choice")