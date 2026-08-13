import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import secrets
import string


# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()


# ==========================================
# PASSWORD MANAGER CLASS
# ==========================================

class PasswordManager:

    def __init__(self, root):

        self.root = root

        self.root.title("Password Manager")
        self.root.geometry("850x600")
        self.root.resizable(False, False)

        self.create_widgets()
        self.load_passwords()


    # ======================================
    # CREATE GUI
    # ======================================

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Password Manager",
            font=("Arial", 26, "bold")
        )

        title.pack(pady=20)


        # ----------------------------------
        # INPUT FRAME
        # ----------------------------------

        input_frame = tk.Frame(self.root)

        input_frame.pack(pady=10)


        # Website

        tk.Label(
            input_frame,
            text="Website:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.website_entry = tk.Entry(
            input_frame,
            width=35
        )

        self.website_entry.grid(
            row=0,
            column=1,
            padx=10
        )


        # Username

        tk.Label(
            input_frame,
            text="Username:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.username_entry = tk.Entry(
            input_frame,
            width=35
        )

        self.username_entry.grid(
            row=1,
            column=1,
            padx=10
        )


        # Password

        tk.Label(
            input_frame,
            text="Password:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.password_entry = tk.Entry(
            input_frame,
            width=35,
            show="*"
        )

        self.password_entry.grid(
            row=2,
            column=1,
            padx=10
        )


        # ----------------------------------
        # BUTTON FRAME
        # ----------------------------------

        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=15)


        tk.Button(
            button_frame,
            text="Generate Password",
            width=18,
            command=self.generate_password
        ).grid(
            row=0,
            column=0,
            padx=5
        )


        tk.Button(
            button_frame,
            text="Add Password",
            width=18,
            command=self.add_password
        ).grid(
            row=0,
            column=1,
            padx=5
        )


        tk.Button(
            button_frame,
            text="Update",
            width=18,
            command=self.update_password
        ).grid(
            row=0,
            column=2,
            padx=5
        )


        tk.Button(
            button_frame,
            text="Delete",
            width=18,
            command=self.delete_password
        ).grid(
            row=0,
            column=3,
            padx=5
        )


        # ----------------------------------
        # SEARCH
        # ----------------------------------

        search_frame = tk.Frame(self.root)

        search_frame.pack(pady=10)


        tk.Label(
            search_frame,
            text="Search Website:"
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        self.search_entry = tk.Entry(
            search_frame,
            width=30
        )

        self.search_entry.pack(
            side=tk.LEFT,
            padx=5
        )


        tk.Button(
            search_frame,
            text="Search",
            width=12,
            command=self.search_passwords
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        tk.Button(
            search_frame,
            text="Show All",
            width=12,
            command=self.load_passwords
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        # ----------------------------------
        # PASSWORD TABLE
        # ----------------------------------

        table_frame = tk.Frame(self.root)

        table_frame.pack(pady=15)


        columns = (
            "ID",
            "Website",
            "Username",
            "Password"
        )


        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )


        widths = {
            "ID": 50,
            "Website": 180,
            "Username": 200,
            "Password": 250
        }


        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=widths[column]
            )


        self.tree.pack(
            side=tk.LEFT
        )


        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )


        self.tree.configure(
            yscrollcommand=scrollbar.set
        )


        self.tree.bind(
            "<ButtonRelease-1>",
            self.select_password
        )


    # ======================================
    # GENERATE PASSWORD
    # ======================================

    def generate_password(self):

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = "".join(
            secrets.choice(characters)
            for _ in range(16)
        )

        self.password_entry.delete(
            0,
            tk.END
        )

        self.password_entry.insert(
            0,
            password
        )


    # ======================================
    # ADD PASSWORD
    # ======================================

    def add_password(self):

        website = self.website_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get()


        if not website or not username or not password:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )

            return


        cursor.execute("""
            INSERT INTO passwords
            (website, username, password)
            VALUES (?, ?, ?)
        """, (
            website,
            username,
            password
        ))


        conn.commit()


        messagebox.showinfo(
            "Success",
            "Password saved successfully!"
        )


        self.clear_fields()
        self.load_passwords()


    # ======================================
    # LOAD PASSWORDS
    # ======================================

    def load_passwords(self):

        for item in self.tree.get_children():

            self.tree.delete(item)


        cursor.execute("""
            SELECT *
            FROM passwords
            ORDER BY website
        """)


        passwords = cursor.fetchall()


        for record in passwords:

            self.tree.insert(
                "",
                tk.END,
                values=record
            )


    # ======================================
    # SELECT PASSWORD
    # ======================================

    def select_password(self, event):

        selected = self.tree.focus()


        if not selected:

            return


        values = self.tree.item(
            selected,
            "values"
        )


        self.clear_fields()


        self.selected_id = values[0]


        self.website_entry.insert(
            0,
            values[1]
        )

        self.username_entry.insert(
            0,
            values[2]
        )

        self.password_entry.insert(
            0,
            values[3]
        )


    # ======================================
    # UPDATE PASSWORD
    # ======================================

    def update_password(self):

        if not hasattr(self, "selected_id"):

            messagebox.showwarning(
                "No Selection",
                "Select a password first."
            )

            return


        website = self.website_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get()


        if not website or not username or not password:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )

            return


        cursor.execute("""
            UPDATE passwords
            SET website=?,
                username=?,
                password=?
            WHERE id=?
        """, (
            website,
            username,
            password,
            self.selected_id
        ))


        conn.commit()


        messagebox.showinfo(
            "Success",
            "Password updated successfully!"
        )


        self.clear_fields()
        self.load_passwords()


    # ======================================
    # DELETE PASSWORD
    # ======================================

    def delete_password(self):

        if not hasattr(self, "selected_id"):

            messagebox.showwarning(
                "No Selection",
                "Select a password first."
            )

            return


        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Delete this password?"
        )


        if confirm:

            cursor.execute(
                "DELETE FROM passwords WHERE id=?",
                (self.selected_id,)
            )


            conn.commit()


            messagebox.showinfo(
                "Success",
                "Password deleted successfully!"
            )


            self.clear_fields()
            self.load_passwords()


    # ======================================
    # SEARCH
    # ======================================

    def search_passwords(self):

        keyword = self.search_entry.get().strip()


        if not keyword:

            self.load_passwords()

            return


        for item in self.tree.get_children():

            self.tree.delete(item)


        cursor.execute("""
            SELECT *
            FROM passwords
            WHERE website LIKE ?
               OR username LIKE ?
        """, (
            "%" + keyword + "%",
            "%" + keyword + "%"
        ))


        passwords = cursor.fetchall()


        for record in passwords:

            self.tree.insert(
                "",
                tk.END,
                values=record
            )


    # ======================================
    # CLEAR FIELDS
    # ======================================

    def clear_fields(self):

        self.website_entry.delete(
            0,
            tk.END
        )

        self.username_entry.delete(
            0,
            tk.END
        )

        self.password_entry.delete(
            0,
            tk.END
        )


        if hasattr(self, "selected_id"):

            del self.selected_id


# ==========================================
# MAIN
# ==========================================

root = tk.Tk()

app = PasswordManager(root)


def close_application():

    conn.close()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)

root.mainloop()