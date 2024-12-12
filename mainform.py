import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime


# Connect to the MySQL database (phpMyAdmin)
db_connection = mysql.connector.connect(
    host="localhost",       # Change to your MySQL server if different
    user="root",            # Your MySQL username
    password="",    # Your MySQL password
    database="library"      # The name of your database (make sure it matches your phpMyAdmin setup)
)
cursor = db_connection.cursor()

# Function to add a record
def add_record():
    name = book_name_entry.get()
    author = author_entry.get()
    book_type = book_type_entry.get()

    if not name or not author or not book_type:
        messagebox.showwarning("Input Error", "All fields must be filled out!")
        return

    book_number = get_next_book_number()

    added_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO books (book_number, name, author, book_type, added_time)
        VALUES (%s, %s, %s, %s, %s)
    ''', (book_number, name, author, book_type, added_time))
    db_connection.commit()

    book_table.insert("", tk.END, values=(book_number, name, author, book_type, added_time))
    clear_entries()
    messagebox.showinfo("Success", "Book added successfully!")

# Function to get the next book number
def get_next_book_number():
    cursor.execute('SELECT MAX(book_number) FROM books')
    result = cursor.fetchone()[0]
    return result + 1 if result else 1

# Function to update a selected record
def update_record():
    selected_item = book_table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    current_values = book_table.item(selected_item, 'values')

    name = book_name_entry.get() or current_values[1]
    author = author_entry.get() or current_values[2]
    book_type = book_type_entry.get() or current_values[3]

    cursor.execute('''
        UPDATE books 
        SET name=%s, author=%s, book_type=%s 
        WHERE book_number=%s
    ''', (name, author, book_type, current_values[0]))
    db_connection.commit()

    book_table.item(selected_item, values=(current_values[0], name, author, book_type, current_values[4]))
    clear_entries()
    messagebox.showinfo("Success", "Book updated successfully!")

# Function to delete a selected record
def delete_record():
    selected_item = book_table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    book_number = book_table.item(selected_item, 'values')[0]
    cursor.execute('DELETE FROM books WHERE book_number=%s', (book_number,))
    db_connection.commit()

    book_table.delete(selected_item)
    messagebox.showinfo("Success", "Book deleted successfully!")

# Function to clear input fields
def clear_entries():
    for entry in [book_name_entry, author_entry, book_type_entry]:
        entry.delete(0, tk.END)

# Function to populate the table with data from the database
def populate_table():
    for row in book_table.get_children():
        book_table.delete(row)

    cursor.execute('SELECT * FROM books')
    for row in cursor.fetchall():
        book_table.insert("", tk.END, values=row[1:])  # Skip the ID field

# Main form
def open_main_form():
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("800x600")
    root.configure(bg="#f5f5f5")

    header = tk.Label(root, text="Library Management System", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white", pady=10)
    header.pack(fill=tk.X)

    frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
    frame.pack(fill=tk.X)

    global book_name_entry, author_entry, book_type_entry, book_table
    tk.Label(frame, text="Name of the Book:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, sticky=tk.E, pady=5)
    book_name_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    book_name_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Author:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, sticky=tk.E, pady=5)
    author_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    author_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Type of Book:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, sticky=tk.E, pady=5)
    book_type_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    book_type_entry.grid(row=2, column=1, pady=5)

    button_frame = tk.Frame(frame, bg="#f5f5f5")
    button_frame.grid(row=3, column=0, columnspan=2, pady=15)

    tk.Button(button_frame, text="Add", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=add_record).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Update", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=update_record).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Delete", font=("Arial", 12, "bold"), bg="#F44336", fg="white", command=delete_record).pack(side=tk.LEFT, padx=5)

    table_frame = tk.Frame(root, bg="#f5f5f5")
    table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    columns = ("Book Number", "Name of the Book", "Author", "Type of Book", "Added Time")
    book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    book_table.heading("Book Number", text="No#")
    book_table.heading("Name of the Book", text="Name of the Book")
    book_table.heading("Author", text="Author")
    book_table.heading("Type of Book", text="Type of Book")
    book_table.heading("Added Time", text="Added Time")
    book_table.column("Book Number", width=50, anchor=tk.CENTER)
    book_table.column("Name of the Book", width=200, anchor=tk.CENTER)
    book_table.column("Author", width=150, anchor=tk.CENTER)
    book_table.column("Type of Book", width=150, anchor=tk.CENTER)
    book_table.column("Added Time", width=150, anchor=tk.CENTER)
    book_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=book_table.yview)
    book_table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    populate_table()
    root.mainloop()

open_main_form()
