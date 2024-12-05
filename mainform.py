import tkinter as tk

def add_record():
    # Logic for adding a record
    print("Add button clicked")

def update_record():
    # Logic for updating a record
    print("Update button clicked")

def delete_record():
    # Logic for deleting a record
    print("Delete button clicked")

root = tk.Tk()
root.title("Library Management System")

Title = tk.Label(root, text="Library Management System", pady=50)
Title.pack()

frame = tk.Frame(root, padx=50, pady=50, borderwidth=5)
frame.pack(padx=50, pady=50)

Record_section = tk.Label(frame, text="Record Section")
Record_section.grid(row=0, column=0, columnspan=2, pady=(0, 10))

Name_of_the_book = tk.Label(frame, text="Name of The Book : ")
Name_of_the_book.grid(row=1, column=0, sticky=tk.E, pady=5)
Name_of_the_book_entry = tk.Entry(frame)
Name_of_the_book_entry.grid(row=1, column=1, pady=5)

Author = tk.Label(frame, text="Author : ")
Author.grid(row=2, column=0, sticky=tk.E, pady=5)
Author_entry = tk.Entry(frame)
Author_entry.grid(row=2, column=1, pady=5)

# Adding the "Type of Book" field
Type_of_book = tk.Label(frame, text="Type of Book : ")
Type_of_book.grid(row=3, column=0, sticky=tk.E, pady=5)
Type_of_book_entry = tk.Entry(frame)
Type_of_book_entry.grid(row=3, column=1, pady=5)

# Adding buttons for Add, Update, and Delete
add_button = tk.Button(frame, text="Add", command=add_record)
add_button.grid(row=4, column=0, pady=10)

update_button = tk.Button(frame, text="Update", command=update_record)
update_button.grid(row=4, column=1, pady=10)

delete_button = tk.Button(frame, text="Delete", command=delete_record)
delete_button.grid(row=4, column=2, pady=10)


root.mainloop()