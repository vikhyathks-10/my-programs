def cafeteria_order():
    menu = {
        1: ("Tea", 10),
        2: ("Coffee", 15),
        3: ("Sandwich", 30),
        4: ("Cake", 25)
        }
    print("Cafeteria Menu:")
    for num, (item, price) in menu.items():
        print(f"{num}. {item} - Rs {price}")

    order={}
    while True:
        choice = input("Enter item number to order or 'done' to finish: ")
        if choice.lower() == "done":
            break
        if not choice.isdigit() or int(choice) not in menu:
            print("Invalid choice, try again.")
            continue
        item_num = int(choice)
        qty = input("Enter quantity: ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity, try again.")
            continue
        qty = int(qty)
        if item_num in order:
            order[item_num] += qty
        else:
            order[item_num] = qty

    total = 0
    print("\nOrder Summary:")
    for item_num, qty in order.items():
        item, price = menu[item_num]
        cost = price * qty
        total += cost
        print(f"{item} x {qty} = Rs {cost}")
    print(f"Total Bill: Rs {total}")

cafeteria_order()



