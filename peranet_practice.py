import sqlite3

import tkinter as tk
from tkinter import messagebox, dialog

connection = None

def connection_db():
    global connection
    try:
        connection = sqlite3.connect("testing_db")
        cursor = connection.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXIST user_account (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL
                    password TEXT NOT NULL
                    )
                    ''')
        connection.commit()
        messagebox.showinfo("Database Connection", "Succesfully connnected to testing")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(a))

root = tk.Tk()
root.title("Crud")
root.geometry("500x300")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Connect Database", command=connection_db)

root.mainloop()