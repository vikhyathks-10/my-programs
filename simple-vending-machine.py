def simple_vending_machine():
    items = {
        1: ("Chips", 20),
        2: ("Soda", 30),
        3: ("Chocolate", 40),
        4: ("Cookies", 25)
    }
    
    print("Welcome to the Vending Machine!")
    while True:
        print("\nItems available:")
        for num, (item, price) in items.items():
            print(f"{num}. {item} - Rs {price}")
        
        choice = input("Enter item number to buy or 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Thank you!")
            break
        if not choice.isdigit() or int(choice) not in items:
            print("Invalid choice.")
            continue
        
        item_num = int(choice)
        qty = input(f"Enter quantity of {items[item_num][0]}: ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity.")
            continue
        
        qty = int(qty)
        total_price = items[item_num][1] * qty
        print(f"Total price: Rs {total_price}")
        print(f"Dispensing {qty} {items[item_num][0]}... Enjoy!")

simple_vending_machine()
