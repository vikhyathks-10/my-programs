# 🔹 DAY 20 - INVENTORY MANAGEMENT SYSTEM

import csv
import os


class InventorySystem:

    FILE_NAME = "inventory.csv"

    # =====================================
    # 🔹 Load Products
    # =====================================

    def load_products(self):

        products = []

        if os.path.exists(self.FILE_NAME):

            with open(self.FILE_NAME,
                      "r",
                      newline="") as file:

                reader = csv.reader(file)

                products = list(reader)

        return products

    # =====================================
    # 🔹 Save Products
    # =====================================

    def save_products(self, products):

        with open(self.FILE_NAME,
                  "w",
                  newline="") as file:

            writer = csv.writer(file)

            writer.writerows(products)

    # =====================================
    # 🔹 Add Product
    # =====================================

    def add_product(self):

        product_id = input("Enter Product ID: ")

        product_name = input(
            "Enter Product Name: "
        )

        stock = input(
            "Enter Stock Quantity: "
        )

        products = self.load_products()

        products.append([
            product_id,
            product_name,
            stock
        ])

        self.save_products(products)

        print("✅ Product Added")

    # =====================================
    # 🔹 Update Stock
    # =====================================

    def update_stock(self):

        product_id = input(
            "Enter Product ID: "
        )

        products = self.load_products()

        found = False

        for product in products:

            if product[0] == product_id:

                new_stock = input(
                    "Enter New Stock: "
                )

                product[2] = new_stock

                found = True

                break

        if found:

            self.save_products(products)

            print("✅ Stock Updated")

        else:

            print("❌ Product Not Found")

    # =====================================
    # 🔹 Delete Product
    # =====================================

    def delete_product(self):

        product_id = input(
            "Enter Product ID: "
        )

        products = self.load_products()

        updated_products = []

        found = False

        for product in products:

            if product[0] != product_id:

                updated_products.append(product)

            else:

                found = True

        if found:

            self.save_products(updated_products)

            print("✅ Product Deleted")

        else:

            print("❌ Product Not Found")

    # =====================================
    # 🔹 Search Product
    # =====================================

    def search_product(self):

        product_id = input(
            "Enter Product ID: "
        )

        products = self.load_products()

        found = False

        for product in products:

            if product[0] == product_id:

                print("\nProduct Found")

                print(
                    f"ID: {product[0]}"
                )

                print(
                    f"Name: {product[1]}"
                )

                print(
                    f"Stock: {product[2]}"
                )

                found = True

                break

        if not found:

            print("❌ Product Not Found")

    # =====================================
    # 🔹 Generate Stock Report
    # =====================================

    def stock_report(self):

        products = self.load_products()

        if not products:

            print("No Products Found")

            return

        print("\n===== STOCK REPORT =====")

        total_stock = 0

        for product in products:

            print(
                f"ID: {product[0]} | "
                f"Name: {product[1]} | "
                f"Stock: {product[2]}"
            )

            total_stock += int(product[2])

        print(
            f"\nTotal Stock Items: {total_stock}"
        )


# =====================================
# 🔹 MAIN PROGRAM
# =====================================

inventory = InventorySystem()

while True:

    print("\n===== INVENTORY SYSTEM =====")

    print("1. Add Product")
    print("2. Update Stock")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Generate Stock Report")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        inventory.add_product()

    elif choice == "2":

        inventory.update_stock()

    elif choice == "3":

        inventory.delete_product()

    elif choice == "4":

        inventory.search_product()

    elif choice == "5":

        inventory.stock_report()

    elif choice == "6":

        print("Goodbye 👋")

        break

    else:

        print("❌ Invalid Choice")