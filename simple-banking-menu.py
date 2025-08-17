def banking_menu():
    balance = 1000  
    while True:
        print("\nMenu: 1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
        choice = input("Choose option: ")
        if choice == '1':
            amt = input("Enter deposit amount: ")
            if amt.isdigit() and int(amt) > 0:
                balance += int(amt)
                print(f"Deposited Rs {amt}. New balance: Rs {balance}")
            else:
                print("Invalid amount.")
        elif choice == '2':
            amt = input("Enter withdrawal amount: ")
            if amt.isdigit() and 0 < int(amt) <= balance:
                balance -= int(amt)
                print(f"Withdrew Rs {amt}. New balance: Rs {balance}")
            else:
                print("Invalid amount or insufficient balance.")
        elif choice == '3':
            print(f"Current balance: Rs {balance}")
        elif choice == '4':
            print("Exiting banking menu.")
            break
        else:
            print("Invalid option.")

banking_menu()
