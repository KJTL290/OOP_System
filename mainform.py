from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

def open_main_form():
    # Database connection setup
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library"
    )
    cursor = db_connection.cursor()

    # Main application window
    root = Tk()
    root.title("Library Management System")
    root.geometry("800x600")

    # Header
    header = Label(root, text="Library Management System", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white", pady=10)
    header.pack(fill=X)

    # Frame for form inputs
    frame = Frame(root, bg="#f5f5f5", padx=20, pady=20)
    frame.pack(fill=X)

    # Input fields
    Label(frame, text="Name of the Book:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, sticky=E, pady=5)
    book_name_entry = Entry(frame, width=30, font=("Arial", 12))
    book_name_entry.grid(row=0, column=1, pady=5)

    Label(frame, text="Author:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, sticky=E, pady=5)
    author_entry = Entry(frame, width=30, font=("Arial", 12))
    author_entry.grid(row=1, column=1, pady=5)

    Label(frame, text="Type of Book:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, sticky=E, pady=5)
    book_type_entry = Entry(frame, width=30, font=("Arial", 12))
    book_type_entry.grid(row=2, column=1, pady=5)

    # Button actions
    def add_record():
        name = book_name_entry.get()
        author = author_entry.get()
        book_type = book_type_entry.get()

        if not name or not author or not book_type:
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return

        book_number = get_next_book_number()
        added_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO books (book_number, name, author, book_type, added_time) VALUES (%s, %s, %s, %s, %s)",
            (book_number, name, author, book_type, added_time)
        )
        db_connection.commit()
        book_table.insert("", END, values=(book_number, name, author, book_type, added_time))
        clear_entries()
        messagebox.showinfo("Success", "Book added successfully!")

    def get_next_book_number():
        cursor.execute("SELECT MAX(book_number) FROM books")
        result = cursor.fetchone()[0]
        return result + 1 if result else 1

    def update_record():
        selected_item = book_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No record selected!")
            return

        current_values = book_table.item(selected_item, 'values')
        name = book_name_entry.get() or current_values[1]
        author = author_entry.get() or current_values[2]
        book_type = book_type_entry.get() or current_values[3]

        cursor.execute(
            "UPDATE books SET name=%s, author=%s, book_type=%s WHERE book_number=%s",
            (name, author, book_type, current_values[0])
        )
        db_connection.commit()
        book_table.item(selected_item, values=(current_values[0], name, author, book_type, current_values[4]))
        clear_entries()
        messagebox.showinfo("Success", "Book updated successfully!")

    def delete_record():
        selected_item = book_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No record selected!")
            return

        book_number = book_table.item(selected_item, 'values')[0]
        cursor.execute("DELETE FROM books WHERE book_number=%s", (book_number,))
        db_connection.commit()
        book_table.delete(selected_item)
        messagebox.showinfo("Success", "Book deleted successfully!")

    def clear_entries():
        for entry in [book_name_entry, author_entry, book_type_entry]:
            entry.delete(0, END)

    # Buttons
    button_frame = Frame(frame, bg="#f5f5f5")
    button_frame.grid(row=3, column=0, columnspan=2, pady=15)

    Button(button_frame, text="Add", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=add_record).pack(side=LEFT, padx=5)
    Button(button_frame, text="Update", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=update_record).pack(side=LEFT, padx=5)
    Button(button_frame, text="Delete", font=("Arial", 12, "bold"), bg="#F44336", fg="white", command=delete_record).pack(side=LEFT, padx=5)

    # Table for displaying records
    table_frame = Frame(root, bg="#f5f5f5")
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    columns = ("Book Number", "Name of the Book", "Author", "Type of Book", "Added Time")
    book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    book_table.heading("Book Number", text="No#")
    book_table.heading("Name of the Book", text="Name of the Book")
    book_table.heading("Author", text="Author")
    book_table.heading("Type of Book", text="Type of Book")
    book_table.heading("Added Time", text="Added Time")
    book_table.column("Book Number", width=50, anchor=CENTER)
    book_table.column("Name of the Book", width=200, anchor=CENTER)
    book_table.column("Author", width=150, anchor=CENTER)
    book_table.column("Type of Book", width=150, anchor=CENTER)
    book_table.column("Added Time", width=150, anchor=CENTER)
    book_table.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=book_table.yview)
    book_table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    def populate_table():
        for row in book_table.get_children():
            book_table.delete(row)

        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            book_table.insert("", END, values=row[1:])

    populate_table()
    root.mainloop()

open_main_form()
