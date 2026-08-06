import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL
)
""")

conn.commit()


class Inventory:

    def add_product(self):

        pid = int(input("Product ID: "))
        name = input("Product Name: ")
        category = input("Category: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        cursor.execute(
            "INSERT INTO products VALUES (?,?,?,?,?)",
            (pid, name, category, quantity, price)
        )

        conn.commit()

        print("Product Added Successfully!")

    def view_products(self):

        cursor.execute("SELECT * FROM products")

        products = cursor.fetchall()

        print("\n========== PRODUCTS ==========\n")

        for product in products:
            print(product)

    def search_product(self):

        pid = int(input("Enter Product ID: "))

        cursor.execute(
            "SELECT * FROM products WHERE product_id=?",
            (pid,)
        )

        product = cursor.fetchone()

        if product:
            print(product)
        else:
            print("Product Not Found.")

    def update_stock(self):

        pid = int(input("Enter Product ID: "))
        quantity = int(input("New Quantity: "))

        cursor.execute(
            "UPDATE products SET quantity=? WHERE product_id=?",
            (quantity, pid)
        )

        conn.commit()

        print("Stock Updated Successfully!")

    def update_price(self):

        pid = int(input("Enter Product ID: "))
        price = float(input("New Price: "))

        cursor.execute(
            "UPDATE products SET price=? WHERE product_id=?",
            (price, pid)
        )

        conn.commit()

        print("Price Updated Successfully!")

    def delete_product(self):

        pid = int(input("Enter Product ID: "))

        cursor.execute(
            "DELETE FROM products WHERE product_id=?",
            (pid,)
        )

        conn.commit()

        print("Product Deleted Successfully!")

    def total_inventory_value(self):

        cursor.execute("SELECT quantity, price FROM products")

        total = 0

        for quantity, price in cursor.fetchall():
            total += quantity * price

        print(f"\nTotal Inventory Value : ₹{total:.2f}")


inventory = Inventory()

while True:

    print("\n========== INVENTORY MANAGEMENT ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Update Price")
    print("6. Delete Product")
    print("7. Total Inventory Value")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        inventory.add_product()

    elif choice == "2":
        inventory.view_products()

    elif choice == "3":
        inventory.search_product()

    elif choice == "4":
        inventory.update_stock()

    elif choice == "5":
        inventory.update_price()

    elif choice == "6":
        inventory.delete_product()

    elif choice == "7":
        inventory.total_inventory_value()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")

conn.close()