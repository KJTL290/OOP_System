import tkinter as tk
import mainform

def on_login():
    username = username_entry.get()
    email = email_entry.get()
    print(f"Username: {username}")
    print(f"Email: {email}")
    root.destroy()
    mainform.open_main_form()  # Call the function to open the main form

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
