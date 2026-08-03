# 06_contact_book.py

import json
import os

FILENAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Name: ")
        phone = input("Phone: ")

        contacts[name] = phone
        save_contacts(contacts)

        print("Contact Added Successfully.")

    elif choice == "2":

        if contacts:

            print("\nSaved Contacts")

            for name, phone in contacts.items():
                print(f"{name} : {phone}")

        else:
            print("No Contacts Found.")

    elif choice == "3":

        name = input("Enter Name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact Not Found.")

    elif choice == "4":

        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Contact Deleted Successfully.")
        else:
            print("Contact Not Found.")

    elif choice == "5":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")