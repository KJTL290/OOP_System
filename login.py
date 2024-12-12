from tkinter import *
from tkinter import messagebox
import mysql.connector
import mainform  # Import the mainform module
from datetime import datetime

def login_form():
    # Create the main window for the login form
    root = Tk()
    root.title("Login Form")
    root.geometry("400x300")

    # Create a frame to act as a box for the login form
    box_frame = Frame(root, bd=2, relief="solid", padx=20, pady=20)
    box_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Create a label for the login form title
    title_label = Label(box_frame, text="Log In", font=("Arial", 16))
    title_label.pack(pady=10)

    # Create a frame to hold the username and password fields
    frame = Frame(box_frame)
    frame.pack(pady=20)

    # Create a label and entry for the username
    username_label = Label(frame, text="Username:", font=("Arial", 12))
    username_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
    username_entry = Entry(frame, width=30, font=("Arial", 12))
    username_entry.grid(row=0, column=1, pady=5)

    # Create a label and entry for the password
    password_label = Label(frame, text="Password:", font=("Arial", 12))
    password_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
    password_entry = Entry(frame, width=30, font=("Arial", 12), show='*')
    password_entry.grid(row=1, column=1, pady=5)

    # Function to handle login button click
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Connect to the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",  # Default username
                password="",  # Default password (leave empty if not set)
                database="login"  # Database name
            )
            cursor = conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            print(f"Error: {err}")  # Print error to the console for debugging
            return  # Exit the function if connection fails

        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Check credentials
        if username == "admin" and password == "password":  # Replace with actual credentials
            status = "Success"
            messagebox.showinfo("Login Successful", "Welcome Admin")
            root.destroy()  # Close the login window
            mainform.open_main_form()  # Call the function to open the main form
        else:
            status = "Failed"
            messagebox.showwarning("Login Failed", "Invalid username or password")

        # Insert login attempt into the database
        try:
            cursor.execute(
                "INSERT INTO login_attempts (username, timestamp, status) VALUES (%s, %s, %s)",
                (username, timestamp, status)
            )
            conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to log attempt: {err}")
            print(f"Failed to log attempt: {err}")
        finally:
            cursor.close()
            conn.close()  # Always close the connection

    # Create a login button
    login_button = Button(box_frame, text="Login", font=("Arial", 12), command=login)
    login_button.pack(pady=20)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    login_form()
