import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT
)
""")

conn.commit()


# ==========================================
# CONTACT BOOK CLASS
# ==========================================

class ContactBook:

    def __init__(self, root):

        self.root = root

        self.root.title("Contact Book")
        self.root.geometry("950x650")
        self.root.resizable(False, False)

        self.create_widgets()
        self.load_contacts()


    # ======================================
    # CREATE GUI
    # ======================================

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Contact Book",
            font=("Arial", 26, "bold")
        )

        title.pack(pady=15)


        # ----------------------------------
        # INPUT FRAME
        # ----------------------------------

        input_frame = tk.Frame(self.root)

        input_frame.pack(pady=10)


        # Name

        tk.Label(
            input_frame,
            text="Name:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.name_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.name_entry.grid(
            row=0,
            column=1,
            padx=10
        )


        # Phone

        tk.Label(
            input_frame,
            text="Phone:"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.phone_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.phone_entry.grid(
            row=0,
            column=3,
            padx=10
        )


        # Email

        tk.Label(
            input_frame,
            text="Email:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.email_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.email_entry.grid(
            row=1,
            column=1,
            padx=10
        )


        # Address

        tk.Label(
            input_frame,
            text="Address:"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.address_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.address_entry.grid(
            row=1,
            column=3,
            padx=10
        )


        # ----------------------------------
        # BUTTON FRAME
        # ----------------------------------

        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=10)


        tk.Button(
            button_frame,
            text="Add Contact",
            width=15,
            command=self.add_contact
        ).grid(
            row=0,
            column=0,
            padx=5
        )


        tk.Button(
            button_frame,
            text="Update",
            width=15,
            command=self.update_contact
        ).grid(
            row=0,
            column=1,
            padx=5
        )


        tk.Button(
            button_frame,
            text="Delete",
            width=15,
            command=self.delete_contact
        ).grid(
            row=0,
            column=2,
            padx=5
        )


        tk.Button(
            button_frame,
            text="Clear",
            width=15,
            command=self.clear_fields
        ).grid(
            row=0,
            column=3,
            padx=5
        )


        # ----------------------------------
        # SEARCH FRAME
        # ----------------------------------

        search_frame = tk.Frame(self.root)

        search_frame.pack(pady=10)


        tk.Label(
            search_frame,
            text="Search:"
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        self.search_entry = tk.Entry(
            search_frame,
            width=35
        )

        self.search_entry.pack(
            side=tk.LEFT,
            padx=5
        )


        tk.Button(
            search_frame,
            text="Search",
            width=12,
            command=self.search_contacts
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        tk.Button(
            search_frame,
            text="Show All",
            width=12,
            command=self.load_contacts
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        # ----------------------------------
        # CONTACT TABLE
        # ----------------------------------

        table_frame = tk.Frame(self.root)

        table_frame.pack(
            pady=15
        )


        columns = (
            "ID",
            "Name",
            "Phone",
            "Email",
            "Address"
        )


        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=14
        )


        column_widths = {
            "ID": 50,
            "Name": 150,
            "Phone": 130,
            "Email": 200,
            "Address": 250
        }


        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=column_widths[column]
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
            self.select_contact
        )


    # ======================================
    # ADD CONTACT
    # ======================================

    def add_contact(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()


        if not name or not phone:

            messagebox.showwarning(
                "Missing Information",
                "Name and Phone are required."
            )

            return


        if not phone.isdigit():

            messagebox.showwarning(
                "Invalid Phone",
                "Phone number should contain digits only."
            )

            return


        cursor.execute("""
            INSERT INTO contacts
            (name, phone, email, address)
            VALUES (?, ?, ?, ?)
        """, (
            name,
            phone,
            email,
            address
        ))


        conn.commit()


        messagebox.showinfo(
            "Success",
            "Contact added successfully!"
        )


        self.clear_fields()
        self.load_contacts()


    # ======================================
    # LOAD CONTACTS
    # ======================================

    def load_contacts(self):

        for item in self.tree.get_children():

            self.tree.delete(item)


        cursor.execute("""
            SELECT *
            FROM contacts
            ORDER BY name
        """)


        contacts = cursor.fetchall()


        for contact in contacts:

            self.tree.insert(
                "",
                tk.END,
                values=contact
            )


    # ======================================
    # SELECT CONTACT
    # ======================================

    def select_contact(self, event):

        selected = self.tree.focus()


        if not selected:

            return


        values = self.tree.item(
            selected,
            "values"
        )


        self.clear_fields()


        self.selected_id = values[0]


        self.name_entry.insert(
            0,
            values[1]
        )

        self.phone_entry.insert(
            0,
            values[2]
        )

        self.email_entry.insert(
            0,
            values[3]
        )

        self.address_entry.insert(
            0,
            values[4]
        )


    # ======================================
    # UPDATE CONTACT
    # ======================================

    def update_contact(self):

        if not hasattr(self, "selected_id"):

            messagebox.showwarning(
                "No Selection",
                "Select a contact first."
            )

            return


        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()


        if not name or not phone:

            messagebox.showwarning(
                "Missing Information",
                "Name and Phone are required."
            )

            return


        if not phone.isdigit():

            messagebox.showwarning(
                "Invalid Phone",
                "Phone number should contain digits only."
            )

            return


        cursor.execute("""
            UPDATE contacts
            SET name=?,
                phone=?,
                email=?,
                address=?
            WHERE contact_id=?
        """, (
            name,
            phone,
            email,
            address,
            self.selected_id
        ))


        conn.commit()


        messagebox.showinfo(
            "Success",
            "Contact updated successfully!"
        )


        self.clear_fields()
        self.load_contacts()


    # ======================================
    # DELETE CONTACT
    # ======================================

    def delete_contact(self):

        if not hasattr(self, "selected_id"):

            messagebox.showwarning(
                "No Selection",
                "Select a contact first."
            )

            return


        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this contact?"
        )


        if confirm:

            cursor.execute(
                "DELETE FROM contacts WHERE contact_id=?",
                (self.selected_id,)
            )


            conn.commit()


            messagebox.showinfo(
                "Success",
                "Contact deleted successfully!"
            )


            self.clear_fields()
            self.load_contacts()


    # ======================================
    # SEARCH CONTACTS
    # ======================================

    def search_contacts(self):

        keyword = self.search_entry.get().strip()


        if not keyword:

            self.load_contacts()

            return


        for item in self.tree.get_children():

            self.tree.delete(item)


        cursor.execute("""
            SELECT *
            FROM contacts
            WHERE name LIKE ?
               OR phone LIKE ?
               OR email LIKE ?
        """, (
            "%" + keyword + "%",
            "%" + keyword + "%",
            "%" + keyword + "%"
        ))


        contacts = cursor.fetchall()


        for contact in contacts:

            self.tree.insert(
                "",
                tk.END,
                values=contact
            )


    # ======================================
    # CLEAR FIELDS
    # ======================================

    def clear_fields(self):

        self.name_entry.delete(
            0,
            tk.END
        )

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.email_entry.delete(
            0,
            tk.END
        )

        self.address_entry.delete(
            0,
            tk.END
        )

        if hasattr(self, "selected_id"):

            del self.selected_id


# ==========================================
# MAIN
# ==========================================

root = tk.Tk()

app = ContactBook(root)


def close_application():

    conn.close()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)

root.mainloop()