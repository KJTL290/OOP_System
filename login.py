from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime

def login_form():
    # Initialize the login form window
    root = Tk()
    root.title("Login Form")
    root.geometry("400x300")

    # Create a container frame for the login form
    form_frame = Frame(root, bd=2, relief="solid", padx=20, pady=20)
    form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Add a title label to the form
    Label(form_frame, text="Log In", font=("Arial", 16)).pack(pady=10)

    # Input fields for username and password
    input_frame = Frame(form_frame)
    input_frame.pack(pady=20)

    Label(input_frame, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=E)
    username_entry = Entry(input_frame, width=30, font=("Arial", 12))
    username_entry.grid(row=0, column=1, pady=5)

    Label(input_frame, text="Password:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=E)
    password_entry = Entry(input_frame, width=30, font=("Arial", 12))
    password_entry.grid(row=1, column=1, pady=5)

    # Login function to validate credentials and log attempts
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Connect to the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",  # Default MySQL username
                password="",  # Default MySQL password (leave blank if not set)
                database="login"
            )
            cursor = conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return  # Stop execution if connection fails

        # Record the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Check username and password (this example always logs the attempt)
        status = "Success" if username == "admin" and password == "1234" else "Failed"
        message = "Login Successful" if status == "Success" else "Login Failed"
        messagebox.showinfo("Login Result", message)

        # Log the login attempt
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
            conn.close()  # Ensure the connection is closed

    # Add a login button
    Button(form_frame, text="Login", font=("Arial", 12), command=login).pack(pady=20)

    root.mainloop()  # Start the Tkinter main loop

if __name__ == "__main__":
    login_form()
