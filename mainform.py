import tkinter as tk
from tkinter import ttk, messagebox


# Function to add a record
def add_record():
    name = book_name_entry.get()
    author = author_entry.get()
    book_type = book_type_entry.get()

    if not name or not author or not book_type:
        messagebox.showwarning("Input Error", "All fields must be filled out!")
        return

    book_table.insert("", tk.END, values=(len(book_table.get_children()) + 1, name, author, book_type))
    clear_entries()
    messagebox.showinfo("Success", "Book added successfully!")

# Function to update a selected record
def update_record():
    selected_item = book_table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    # Get current values of the selected item
    current_values = book_table.item(selected_item, 'values')

    # Get new values from the entries, defaulting to current values if entries are empty
    name = book_name_entry.get() or current_values[1]
    author = author_entry.get() or current_values[2]
    book_type = book_type_entry.get() or current_values[3]

    # Update the selected item with new values
    book_table.item(selected_item, values=(current_values[0], name, author, book_type))
    clear_entries()
    messagebox.showinfo("Success", "Book updated successfully!")

# Function to delete a selected record
def delete_record():
    selected_item = book_table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    book_table.delete(selected_item)
    messagebox.showinfo("Success", "Book deleted successfully!")

# Function to clear input fields
def clear_entries():
    for entry in [book_name_entry, author_entry, book_type_entry]:
        entry.delete(0, tk.END)

# Main form
def open_main_form():
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("800x600")
    root.configure(bg="#f5f5f5")  # Set background color

    # Header Label
    header = tk.Label(root, text="Library Management System", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white", pady=10)
    header.pack(fill=tk.X)

    # Input frame
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

    # Table frame
    table_frame = tk.Frame(root, bg="#f5f5f5")
    table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    columns = ("Serial No", "Name of the Book", "Author", "Type of Book")
    book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    book_table.heading("Serial No", text="No#")
    book_table.heading("Name of the Book", text="Name of the Book")
    book_table.heading("Author", text="Author")
    book_table.heading("Type of Book", text="Type of Book")
    book_table.column("Serial No", width=50, anchor=tk.CENTER)
    book_table.column("Name of the Book", width=200, anchor=tk.CENTER)
    book_table.column("Author", width=150, anchor=tk.CENTER)
    book_table.column("Type of Book", width=150, anchor=tk.CENTER)
    book_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=book_table.yview)
    book_table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    root.mainloop()

