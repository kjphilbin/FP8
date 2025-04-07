import sqlite3

# Create database and table for customer information
def create_database():
    conn = sqlite3.connect("customers.db")  # Create or connect to the database
    cursor = conn.cursor()
    # Create the customers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            address TEXT,
            preferred_contact TEXT
        )
    """)
    conn.commit()
    conn.close()

# Call the function to ensure the database is set up
create_database()

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to submit customer info to the database
def submit_customer_info():
    name = name_entry.get().strip()
    birthday = birthday_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    address = address_entry.get("1.0", tk.END).strip()
    preferred_contact = contact_method_var.get()

    if not name or not email or not preferred_contact:
        messagebox.showerror("Error", "Name, Email, and Preferred Contact Method are required!")
        return

    try:
        conn = sqlite3.connect("customers.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO customers (name, birthday, email, phone, address, preferred_contact)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, birthday, email, phone, address, preferred_contact))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer information submitted successfully!")
        clear_form()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email must be unique!")

# Function to clear the form after submission
def clear_form():
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    contact_method_var.set("")

# Create the main window
root = tk.Tk()
root.title("Customer Information Management")

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Birthday
tk.Label(root, text="Birthday (YYYY-MM-DD):").grid(row=1, column=0, pady=5, sticky="w")
birthday_entry = tk.Entry(root, width=30)
birthday_entry.grid(row=1, column=1, pady=5)

# Email
tk.Label(root, text="Email:").grid(row=2, column=0, pady=5, sticky="w")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, pady=5)

# Phone
tk.Label(root, text="Phone:").grid(row=3, column=0, pady=5, sticky="w")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=3, column=1, pady=5)

# Address
tk.Label(root, text="Address:").grid(row=4, column=0, pady=5, sticky="nw")
address_entry = tk.Text(root, width=30, height=4)
address_entry.grid(row=4, column=1, pady=5)

# Preferred Contact Method
tk.Label(root, text="Preferred Contact Method:").grid(row=5, column=0, pady=5, sticky="w")
contact_method_var = tk.StringVar(value="")
contact_method_menu = tk.OptionMenu(root, contact_method_var, "Email", "Phone", "Mail")
contact_method_menu.grid(row=5, column=1, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_customer_info)
submit_button.grid(row=6, column=1, pady=10, sticky="e")

# Run the application
root.mainloop()