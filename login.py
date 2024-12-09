import tkinter as tk
import mainform
import mysql.connector

def on_login():
    username = username_entry.get()
    email = email_entry.get()

    # Connect to the database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='your_database_name'
    )
    cursor = connection.cursor()

    # Insert user data into the database
    add_user = ("INSERT INTO users (username, email) VALUES (%s, %s)")
    user_data = (username, email)
    cursor.execute(add_user, user_data)
    connection.commit()

    # Close the connection
    cursor.close()
    connection.close()

    print(f"Username: {username}")
    print(f"Email: {email}")
    root.destroy()
    mainform.open_main_form()

if __name__ == "__main__":
    # Main Window
    root = tk.Tk()
    root.title("Log In")
    
    # Frame for the login form
    frame = tk.Frame(root, padx=50, pady=50, borderwidth=5)
    frame.pack(padx=50, pady=50)

    username_label = tk.Label(frame, text="Username:")
    username_label.grid(row=1, column=0, sticky=tk.E, pady=5)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1, pady=5)

    email_label = tk.Label(frame, text="Email:")
    email_label.grid(row=2, column=0, sticky=tk.E, pady=5)
    email_entry = tk.Entry(frame)
    email_entry.grid(row=2, column=1, pady=5)

    login_button = tk.Button(frame, text="Log In", command=on_login)
    login_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()