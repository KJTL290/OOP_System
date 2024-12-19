from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

def open_main_form():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="stack"
    )
    cursor = db_connection.cursor()

    root = Tk()
    root.title("Rice and Corn Management System")
    root.geometry("900x600")

    header = Label(
        root,
        text="Rice and Corn Stack Management System",
        font=("Helvetica", 18, "bold"),
        bg="green",
        fg="white",
        pady=10
    )
    header.pack(fill=X)

    input_frame = Frame(root, bg="light grey", padx=20, pady=20)
    input_frame.pack(fill=X)

    season_label = Label(input_frame, text="Type of Season:", font=("Arial", 12), bg="light grey").grid(row=0, column=0, sticky=E, pady=5)
    type_of_season_entry = Entry(input_frame, width=30, font=("Arial", 12))
    type_of_season_entry.grid(row=0, column=1, pady=5)

    location_label = Label(input_frame, text="Location:", font=("Arial", 12), bg="light grey").grid(row=1, column=0, sticky=E, pady=5)
    location_entry = Entry(input_frame, width=30, font=("Arial", 12))
    location_entry.grid(row=1, column=1, pady=5)

    type_of_product = Label(input_frame, text="Type of Product (Rice/Corn):", font=("Arial", 12), bg="light grey").grid(row=2, column=0, sticky=E, pady=5)
    product_type_entry = Entry(input_frame, width=30, font=("Arial", 12))
    product_type_entry.grid(row=2, column=1, pady=5)

    harvest_label = Label(input_frame, text="Number of Harvest:", font=("Arial", 12), bg="light grey").grid(row=3, column=0, sticky=E, pady=5)
    sacks_entry = Entry(input_frame, width=30, font=("Arial", 12))
    sacks_entry.grid(row=3, column=1, pady=5)

    def add_record():
        season = type_of_season_entry.get()
        location = location_entry.get()
        product_type = product_type_entry.get()
        sacks = sacks_entry.get()

        if not season or not location or not product_type or not sacks:
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return

        try:
            sacks = int(sacks)
        except ValueError:
            messagebox.showwarning("Input Error", "Number of sacks must be a valid number!")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            """
            INSERT INTO farm_stack (Type_of_Season, Located, Type_of_Product, Number_of_Sacks, Time_Added)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (season, location, product_type, sacks, timestamp)
        )
        db_connection.commit()
        populate_table()
        clear_inputs()
        messagebox.showinfo("Success", "Record added successfully!")

    def update_record():
        selected_item = stack_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a record to update!")
            return

        stack_number = stack_table.item(selected_item, 'values')[0]
        season = type_of_season_entry.get()
        location = location_entry.get()
        product_type = product_type_entry.get()
        sacks = sacks_entry.get()

        updates = {}

        if season:
            updates['Type_of_Season'] = season
        if location:
            updates['Located'] = location
        if product_type:
            updates['Type_of_Product'] = product_type
        if sacks:
            try:
                updates['Number_of_Sacks'] = int(sacks)
            except ValueError:
                messagebox.showwarning("Input Error", "Number of sacks must be a valid number!")
                return

        if not updates:
            messagebox.showwarning("Input Error", "At least one field must be filled to update!")
            return

        set_clause = ", ".join([f"{key}=%s" for key in updates])
        values = list(updates.values()) + [stack_number]

        query = f"UPDATE farm_stack SET {set_clause} WHERE Stack_Number=%s"
        cursor.execute(query, values)
        db_connection.commit()
        populate_table()
        clear_inputs()
        messagebox.showinfo("Success", "Record updated successfully!")

    def delete_record():
        selected_item = stack_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a record to delete!")
            return

        stack_number = stack_table.item(selected_item, 'values')[0]
        cursor.execute("DELETE FROM farm_stack WHERE Stack_Number=%s", (stack_number,))
        db_connection.commit()
        populate_table()
        clear_inputs()
        messagebox.showinfo("Success", "Record deleted successfully!")

    def clear_inputs():
        for entry in [type_of_season_entry, location_entry, product_type_entry, sacks_entry]:
            entry.delete(0, END)

    button_frame = Frame(input_frame, bg="light grey")
    button_frame.grid(row=4, column=0, columnspan=2, pady=15)

    Button(button_frame, text="Add", font=("Arial", 12, "bold"), bg="green", fg="white", command=add_record).pack(side=LEFT, padx=5)
    Button(button_frame, text="Update", font=("Arial", 12, "bold"), bg="blue", fg="white", command=update_record).pack(side=LEFT, padx=5)
    Button(button_frame, text="Delete", font=("Arial", 12, "bold"), bg="red", fg="white", command=delete_record).pack(side=LEFT, padx=5)

    table_frame = Frame(root, bg="light grey")
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    columns = ("Id#", "Type of Season", "Located", "Type of Product", "Number of Sacks", "Time Added")
    stack_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    for col in columns:
        stack_table.heading(col, text=col)
        stack_table.column(col, anchor=CENTER, width=150)

    stack_table.column("Id#", width=50)
    stack_table.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=stack_table.yview)
    stack_table.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    def populate_table():
        stack_table.delete(*stack_table.get_children())
        cursor.execute("SELECT * FROM farm_stack")
        for row in cursor.fetchall():
            stack_table.insert("", END, values=row)

    populate_table()

    def on_closing():
        cursor.close()
        db_connection.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()