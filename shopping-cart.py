def shopping_cart():
    items = {
        "apple": 20,
        "banana": 10,
        "bread": 40,
        "milk": 30
    }
    cart = {}
    while True:
        print("\nItems available:")
        for item, price in items.items():
            print(f"{item} - Rs {price}")
        action = input("Type 'add', 'remove', 'show', or 'quit': ").lower()

        if action == "add":
            item = input("Enter item to add: ").lower()
            if item not in items:
                print("Item not available.")
                continue
            qty = input("Enter quantity: ")
            if not qty.isdigit() or int(qty) <= 0:
                print("Invalid quantity.")
                continue
            qty = int(qty)
            cart[item] = cart.get(item, 0) + qty
            print(f"Added {qty} {item}(s) to cart.")
        elif action == "remove":
            item = input("Enter item to remove: ").lower()
            if item not in cart:
                print("Item not in cart.")
                continue
            qty = input("Enter quantity to remove: ")
            if not qty.isdigit() or int(qty) <= 0 or int(qty) > cart[item]:
                print("Invalid quantity.")
                continue
            qty = int(qty)
            cart[item] -= qty
            if cart[item] == 0:
                del cart[item]
            print(f"Removed {qty} {item}(s) from cart.")
        elif action == "show":
            if not cart:
                print("Cart is empty.")
                continue
            print("\nCart contents:")
            total = 0
            for item,qty in cart.items():
                cost=items[item]*qty
                total+=cost
            print(f"{item} x {qty} = Rs {cost}")
            print(f"Total cost: Rs {total}")
        elif action == "quit":
            print("Thank you for shopping!")
            break
        else:
                print("Invalid action.")
