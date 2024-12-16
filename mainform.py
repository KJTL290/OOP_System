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
        database="stack"
    )
    cursor = db_connection.cursor()

    # Main application window
    root = Tk()
    root.title("Rice and Corn Management System")
    root.geometry("800x600")

    # Header
    header = Label(root, text="Rice and Corn Stack Management System", font=("Helvetica", 18, "bold"), bg="green", fg="white", pady=10)
    header.pack(fill=X)

    # Frame for form inputs
    frame = Frame(root, bg="light grey", padx=20, pady=20)
    frame.pack(fill=X)

    # Input fields
    Label(frame, text="Name of the Farmer:", font=("Arial", 12), bg="light grey").grid(row=0, column=0, sticky=E, pady=5)
    name_of_farmer = Entry(frame, width=30, font=("Arial", 12))
    name_of_farmer.grid(row=0, column=1, pady=5)

    Label(frame, text="Address of the Farmer:", font=("Arial", 12), bg="light grey").grid(row=1, column=0, sticky=E, pady=5)
    address_of_farmer = Entry(frame, width=30, font=("Arial", 12))
    address_of_farmer.grid(row=1, column=1, pady=5)

    Label(frame, text="Type of Product (Rice/Corn):", font=("Arial", 12), bg="light grey").grid(row=2, column=0, sticky=E, pady=5)
    type_of_product = Entry(frame, width=30, font=("Arial", 12))
    type_of_product.grid(row=2, column=1, pady=5)

    Label(frame, text="Number of Stacks:", font=("Arial", 12), bg="light grey").grid(row=3, column=0, sticky=E, pady=5)
    number_of_stacks = Entry(frame, width=30, font=("Arial", 12))
    number_of_stacks.grid(row=3, column=1, pady=5)

    # Button actions
    def add_record():
        name = name_of_farmer.get()
        address = address_of_farmer.get()
        product_type = type_of_product.get()
        stacks = number_of_stacks.get()

        if not name or not address or not product_type or not stacks:
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return

        try:
            stacks = int(stacks)
        except ValueError:
            messagebox.showwarning("Input Error", "Number of stacks must be a valid number!")
            return

        stack_number = get_next_stack_number()
        added_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO farm_stack (stack_number, name, address, product_type, number_of_stacks, added_time) VALUES (%s, %s, %s, %s, %s, %s)",
            (stack_number, name, address, product_type, stacks, added_time)
        )
        db_connection.commit()
        stack_table.insert("", END, values=(stack_number, name, address, product_type, stacks, added_time))
        clear_entries()
        messagebox.showinfo("Success", "Record added successfully!")

    def get_next_stack_number():
        cursor.execute("SELECT MAX(stack_number) FROM farm_stack")
        result = cursor.fetchone()[0]
        return result + 1 if result else 1

    def update_record():
        selected_item = stack_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No record selected!")
            return

        current_values = stack_table.item(selected_item, 'values')
        name = name_of_farmer.get() or current_values[1]
        address = address_of_farmer.get() or current_values[2]
        product_type = type_of_product.get() or current_values[3]
        stacks = number_of_stacks.get() or current_values[4]

        try:
            stacks = int(stacks)
        except ValueError:
            messagebox.showwarning("Input Error", "Number of stacks must be a valid number!")
            return

        cursor.execute(
            "UPDATE farm_stack SET name=%s, address=%s, product_type=%s, number_of_stacks=%s WHERE stack_number=%s",
            (name, address, product_type, stacks, current_values[0])
        )
        db_connection.commit()
        stack_table.item(selected_item, values=(current_values[0], name, address, product_type, stacks, current_values[5]))
        clear_entries()
        messagebox.showinfo("Success", "Record updated successfully!")

    def delete_record():
        selected_item = stack_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No record selected!")
            return

        stack_number = stack_table.item(selected_item, 'values')[0]
        cursor.execute("DELETE FROM farm_stack WHERE stack_number=%s", (stack_number,))
        db_connection.commit()
        stack_table.delete(selected_item)
        messagebox.showinfo("Success", "Record deleted successfully!")

    def clear_entries():
        for entry in [name_of_farmer, address_of_farmer, type_of_product, number_of_stacks]:
            entry.delete(0, END)

    # Buttons
    button_frame = Frame(frame, bg="light grey")
    button_frame.grid(row=4, column=0, columnspan=2, pady=15)

    Button(button_frame, text="Add", font=("Arial", 12, "bold"), bg="green", fg="white", command=add_record).pack(side=LEFT, padx=5)
    Button(button_frame, text="Update", font=("Arial", 12, "bold"), bg="blue", fg="white", command=update_record).pack(side=LEFT, padx=5)
    Button(button_frame, text="Delete", font=("Arial", 12, "bold"), bg="red", fg="white", command=delete_record).pack(side=LEFT, padx=5)

    # Table for displaying records
    table_frame = Frame(root, bg="light grey")
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    columns = ("Stack Number", "Name of Farmer", "Address", "Type of Product", "Number of Stacks", "Added Time")
    stack_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    stack_table.heading("Stack Number", text="No#")
    stack_table.heading("Name of Farmer", text="Name of Farmer")
    stack_table.heading("Address", text="Address")
    stack_table.heading("Type of Product", text="Type of Product")
    stack_table.heading("Number of Stacks", text="Number of Stacks")
    stack_table.heading("Added Time", text="Added Time")
    stack_table.column("Stack Number", width=50, anchor=CENTER)
    stack_table.column("Name of Farmer", width=200, anchor=CENTER)
    stack_table.column("Address", width=150, anchor=CENTER)
    stack_table.column("Type of Product", width=150, anchor=CENTER)
    stack_table.column("Number of Stacks", width=120, anchor=CENTER)
    stack_table.column("Added Time", width=150, anchor=CENTER)
    stack_table.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=stack_table.yview)
    stack_table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    def populate_table():
        for row in stack_table.get_children():
            stack_table.delete(row)

        cursor.execute("SELECT * FROM farm_stack")
        for row in cursor.fetchall():
            stack_table.insert("", END, values=row[1:])

    populate_table()
    root.mainloop()