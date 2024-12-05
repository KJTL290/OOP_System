import tkinter as tk
from tkinter import ttk, messagebox

# Initialize the book count
book_count = 0

# Function to add a book to the table
def add_record():
    global book_count
    name = Name_of_the_book_entry.get()
    author = Author_entry.get()
    book_type = Type_of_book_entry.get()

    if not name or not author or not book_type:
        messagebox.showwarning("Input Error", "All fields must be filled out!")
        return

    book_count += 1
    book_table.insert("", tk.END, values=(book_count, name, author, book_type))
    Name_of_the_book_entry.delete(0, tk.END)
    Author_entry.delete(0, tk.END)
    Type_of_book_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Book added successfully!")

# Function to update the selected record
def update_record():
    selected = book_table.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    name = Name_of_the_book_entry.get()
    author = Author_entry.get()
    book_type = Type_of_book_entry.get()

    if not name or not author or not book_type:
        messagebox.showwarning("Input Error", "All fields must be filled out!")
        return

    for record in selected:
        # Preserve the serial number
        values = book_table.item(record, "values")
        serial_number = values[0]
        book_table.item(record, values=(serial_number, name, author, book_type))

    Name_of_the_book_entry.delete(0, tk.END)
    Author_entry.delete(0, tk.END)
    Type_of_book_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Book updated successfully!")

# Function to delete the selected record
def delete_record():
    selected = book_table.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    for record in selected:
        book_table.delete(record)

    messagebox.showinfo("Success", "Book deleted successfully!")

# Function to search for a book in the table
def search_record():
    query = search_entry.get().lower()
    for item in book_table.get_children():
        values = book_table.item(item, "values")
        if query in map(str.lower, values):  # Case-insensitive search
            book_table.selection_set(item)
            book_table.focus(item)
            return
    messagebox.showinfo("Not Found", "No matching records found.")

# Main window
root = tk.Tk()
root.title("Library Management System")

# Title
Title = tk.Label(root, text="Library Management System", pady=20, font=("Arial", 16))
Title.pack()

# Input frame
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

Record_section = tk.Label(frame, text="Record Section", font=("Arial", 12, "bold"))
Record_section.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Input fields
Name_of_the_book = tk.Label(frame, text="Name of The Book:")
Name_of_the_book.grid(row=1, column=0, sticky=tk.E, pady=5)
Name_of_the_book_entry = tk.Entry(frame)
Name_of_the_book_entry.grid(row=1, column=1, pady=5)

Author = tk.Label(frame, text="Author:")
Author.grid(row=2, column=0, sticky=tk.E, pady=5)
Author_entry = tk.Entry(frame)
Author_entry.grid(row=2, column=1, pady=5)

Type_of_book = tk.Label(frame, text="Type of Book:")
Type_of_book.grid(row=3, column=0, sticky=tk.E, pady=5)
Type_of_book_entry = tk.Entry(frame)
Type_of_book_entry.grid(row=3, column=1, pady=5)

# Buttons
add_button = tk.Button(frame, text="Add", command=add_record, width=10)
add_button.grid(row=4, column=0, pady=10, padx=5)

update_button = tk.Button(frame, text="Update", command=update_record, width=10)
update_button.grid(row=4, column=1, pady=10, padx=5)

delete_button = tk.Button(frame, text="Delete", command=delete_record, width=10)
delete_button.grid(row=4, column=2, pady=10, padx=5)

# Search field
search_label = tk.Label(frame, text="Search:")
search_label.grid(row=5, column=0, sticky=tk.E, pady=5)
search_entry = tk.Entry(frame)
search_entry.grid(row=5, column=1, pady=5)

search_button = tk.Button(frame, text="Search", command=search_record, width=10)
search_button.grid(row=5, column=2, pady=10, padx=5)

# Table frame
table_frame = tk.Frame(root)
table_frame.pack(padx=20, pady=20)

# Scrollbar
scrollbar = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

# Table
columns = ("Serial No", "Name of the Book", "Author", "Type of Book")
book_table = ttk.Treeview(table_frame, columns=columns, show="headings", yscrollcommand=scrollbar.set)
scrollbar.config(command=book_table.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure table columns
book_table.heading("Serial No", text="No#")
book_table.heading("Name of the Book", text="Name of the Book")
book_table.heading("Author", text="Author")
book_table.heading("Type of Book", text="Type of Book")
book_table.column("Serial No", width=80, anchor=tk.CENTER)
book_table.column("Name of the Book", width=200, anchor=tk.W)
book_table.column("Author", width=150, anchor=tk.W)
book_table.column("Type of Book", width=150, anchor=tk.W)
book_table.pack()

# Run the app
root.mainloop()
