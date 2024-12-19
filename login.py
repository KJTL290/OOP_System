from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from mainform import open_main_form  

def login_form():
    root = Tk()
    root.title("Login Form")
    root.geometry("400x300")

    form_frame = Frame(root, bd=2, relief="solid", padx=20, pady=20)
    form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(form_frame, text="Log In", font=("Arial", 25)).pack(pady=10)

    input_frame = Frame(form_frame)
    input_frame.pack(pady=20)

    Label(input_frame, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=E)
    username_entry = Entry(input_frame, width=30, font=("Arial", 12))
    username_entry.grid(row=0, column=1, pady=5)

    Label(input_frame, text="Password:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=E)
    password_entry = Entry(input_frame, width=30, font=("Arial", 12), show="#")
    password_entry.grid(row=1, column=1, pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="login"
            )
            cursor = conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        status = "Success" if username == "admin" and password == "12345" else "Failed"
        message = "Login Successful" if status == "Success" else "Login Failed"

        try:
            cursor.execute(
                "INSERT INTO login_attempts (username, timestamp, status, typed_password) VALUES (%s, %s, %s, %s)",
                (username, timestamp, status, password)
            )
            conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to log attempt: {err}")
        finally:
            cursor.close()
            conn.close()

        if status == "Success":
            messagebox.showinfo("Login Result", message)
            root.destroy()
            open_main_form()
        else:
            messagebox.showerror("Login Result", message)

    Button(form_frame, text="Login", font=("Arial", 12), command=login).pack(pady=20)

    root.mainloop()
login_form()