import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# ==========================================
# DATABASE
# ==========================================

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

conn.commit()


# ==========================================
# INVENTORY APPLICATION
# ==========================================

class InventoryApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Inventory Management System")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        self.create_widgets()
        self.load_products()


    # ======================================
    # CREATE GUI
    # ======================================

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Inventory Management System",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=15)


        # ----------------------------------
        # INPUT FRAME
        # ----------------------------------

        input_frame = tk.Frame(self.root)

        input_frame.pack(pady=10)


        tk.Label(
            input_frame,
            text="Product ID"
        ).grid(row=0, column=0, padx=10, pady=5)

        self.id_entry = tk.Entry(input_frame)

        self.id_entry.grid(row=0, column=1, padx=10)


        tk.Label(
            input_frame,
            text="Product Name"
        ).grid(row=0, column=2, padx=10)

        self.name_entry = tk.Entry(input_frame)

        self.name_entry.grid(row=0, column=3, padx=10)


        tk.Label(
            input_frame,
            text="Category"
        ).grid(row=1, column=0, padx=10, pady=5)

        self.category_entry = tk.Entry(input_frame)

        self.category_entry.grid(row=1, column=1, padx=10)


        tk.Label(
            input_frame,
            text="Quantity"
        ).grid(row=1, column=2, padx=10)

        self.quantity_entry = tk.Entry(input_frame)

        self.quantity_entry.grid(row=1, column=3, padx=10)


        tk.Label(
            input_frame,
            text="Price"
        ).grid(row=2, column=0, padx=10, pady=5)

        self.price_entry = tk.Entry(input_frame)

        self.price_entry.grid(row=2, column=1, padx=10)


        # ----------------------------------
        # BUTTONS
        # ----------------------------------

        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=10)


        tk.Button(
            button_frame,
            text="Add Product",
            width=15,
            command=self.add_product
        ).grid(row=0, column=0, padx=5)


        tk.Button(
            button_frame,
            text="Update",
            width=15,
            command=self.update_product
        ).grid(row=0, column=1, padx=5)


        tk.Button(
            button_frame,
            text="Delete",
            width=15,
            command=self.delete_product
        ).grid(row=0, column=2, padx=5)


        tk.Button(
            button_frame,
            text="Clear",
            width=15,
            command=self.clear_fields
        ).grid(row=0, column=3, padx=5)


        # ----------------------------------
        # SEARCH
        # ----------------------------------

        search_frame = tk.Frame(self.root)

        search_frame.pack(pady=10)


        tk.Label(
            search_frame,
            text="Search Product:"
        ).pack(side=tk.LEFT, padx=5)


        self.search_entry = tk.Entry(
            search_frame,
            width=30
        )

        self.search_entry.pack(side=tk.LEFT, padx=5)


        tk.Button(
            search_frame,
            text="Search",
            command=self.search_product
        ).pack(side=tk.LEFT, padx=5)


        tk.Button(
            search_frame,
            text="Show All",
            command=self.load_products
        ).pack(side=tk.LEFT, padx=5)


        # ----------------------------------
        # TABLE
        # ----------------------------------

        table_frame = tk.Frame(self.root)

        table_frame.pack(pady=10)


        columns = (
            "ID",
            "Name",
            "Category",
            "Quantity",
            "Price"
        )


        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )


        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=150
            )


        self.tree.pack(side=tk.LEFT)


        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )


        self.tree.bind(
            "<ButtonRelease-1>",
            self.select_product
        )


    # ======================================
    # ADD PRODUCT
    # ======================================

    def add_product(self):

        try:

            product_id = int(
                self.id_entry.get()
            )

            name = self.name_entry.get().strip()

            category = self.category_entry.get().strip()

            quantity = int(
                self.quantity_entry.get()
            )

            price = float(
                self.price_entry.get()
            )


            if not name or not category:

                messagebox.showwarning(
                    "Input Error",
                    "Please enter product name and category."
                )

                return


            if quantity < 0 or price < 0:

                messagebox.showwarning(
                    "Input Error",
                    "Quantity and price cannot be negative."
                )

                return


            cursor.execute("""
                INSERT INTO products
                VALUES (?, ?, ?, ?, ?)
            """, (
                product_id,
                name,
                category,
                quantity,
                price
            ))


            conn.commit()


            messagebox.showinfo(
                "Success",
                "Product added successfully!"
            )


            self.clear_fields()

            self.load_products()


        except ValueError:

            messagebox.showerror(
                "Error",
                "Please enter valid values."
            )


        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Error",
                "Product ID already exists."
            )


    # ======================================
    # LOAD PRODUCTS
    # ======================================

    def load_products(self):

        for item in self.tree.get_children():

            self.tree.delete(item)


        cursor.execute(
            "SELECT * FROM products"
        )

        products = cursor.fetchall()


        for product in products:

            self.tree.insert(
                "",
                tk.END,
                values=product
            )


    # ======================================
    # SELECT PRODUCT
    # ======================================

    def select_product(self, event):

        selected = self.tree.focus()

        if not selected:

            return


        values = self.tree.item(
            selected,
            "values"
        )


        self.clear_fields()


        self.id_entry.insert(
            0,
            values[0]
        )

        self.name_entry.insert(
            0,
            values[1]
        )

        self.category_entry.insert(
            0,
            values[2]
        )

        self.quantity_entry.insert(
            0,
            values[3]
        )

        self.price_entry.insert(
            0,
            values[4]
        )


    # ======================================
    # UPDATE PRODUCT
    # ======================================

    def update_product(self):

        try:

            product_id = int(
                self.id_entry.get()
            )

            name = self.name_entry.get().strip()

            category = self.category_entry.get().strip()

            quantity = int(
                self.quantity_entry.get()
            )

            price = float(
                self.price_entry.get()
            )


            if not name or not category:

                messagebox.showwarning(
                    "Input Error",
                    "Please fill all fields."
                )

                return


            cursor.execute("""
                UPDATE products
                SET product_name=?,
                    category=?,
                    quantity=?,
                    price=?
                WHERE product_id=?
            """, (
                name,
                category,
                quantity,
                price,
                product_id
            ))


            conn.commit()


            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Not Found",
                    "Product not found."
                )

                return


            messagebox.showinfo(
                "Success",
                "Product updated successfully!"
            )


            self.clear_fields()

            self.load_products()


        except ValueError:

            messagebox.showerror(
                "Error",
                "Please enter valid values."
            )


    # ======================================
    # DELETE PRODUCT
    # ======================================

    def delete_product(self):

        try:

            product_id = int(
                self.id_entry.get()
            )


            cursor.execute(
                "SELECT product_name FROM products WHERE product_id=?",
                (product_id,)
            )

            product = cursor.fetchone()


            if not product:

                messagebox.showwarning(
                    "Not Found",
                    "Product not found."
                )

                return


            confirm = messagebox.askyesno(
                "Confirm Delete",
                f"Delete {product[0]}?"
            )


            if confirm:

                cursor.execute(
                    "DELETE FROM products WHERE product_id=?",
                    (product_id,)
                )

                conn.commit()


                messagebox.showinfo(
                    "Success",
                    "Product deleted successfully!"
                )


                self.clear_fields()

                self.load_products()


        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid Product ID."
            )


    # ======================================
    # SEARCH PRODUCT
    # ======================================

    def search_product(self):

        keyword = self.search_entry.get().strip()


        if not keyword:

            self.load_products()

            return


        for item in self.tree.get_children():

            self.tree.delete(item)


        cursor.execute("""
            SELECT *
            FROM products
            WHERE product_name LIKE ?
               OR category LIKE ?
        """, (
            "%" + keyword + "%",
            "%" + keyword + "%"
        ))


        products = cursor.fetchall()


        for product in products:

            self.tree.insert(
                "",
                tk.END,
                values=product
            )


    # ======================================
    # CLEAR FIELDS
    # ======================================

    def clear_fields(self):

        self.id_entry.delete(0, tk.END)

        self.name_entry.delete(0, tk.END)

        self.category_entry.delete(0, tk.END)

        self.quantity_entry.delete(0, tk.END)

        self.price_entry.delete(0, tk.END)


# ==========================================
# MAIN
# ==========================================

root = tk.Tk()

app = InventoryApp(root)

root.mainloop()


# Close database when application exits
conn.close()