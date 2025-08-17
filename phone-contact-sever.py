def phone_contact_saver():
    contacts = {}
    while True:
        action = input("Type 'add' to add contact, 'search' to find, or 'exit' to quit: ").lower()
        if action == 'add':
            name = input("Enter name: ").strip()
            number = input("Enter number: ").strip()
            contacts[name] = number
            print(f"Contact for {name} saved.")
        elif action == 'search':
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"{name}'s number is {contacts[name]}")
            else:
                print(f"No contact found for {name}.")
        elif action == 'exit':
            print("Exiting contact saver.")
            break
        else:
            print("Invalid action.")

phone_contact_saver()
