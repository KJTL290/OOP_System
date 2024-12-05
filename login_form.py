import tkinter as tk
from tkinter import messagebox
import main_form  # Import the main form module

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        # Username and password labels and entries
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        # Login button
        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.pack()

    def open_main_form(self):
        # Destroy the login window and open the main form
        self.root.destroy()
        main_form.open_main_form()

    def login(self):
        # Dummy login logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "password":
            self.open_main_form()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    login_window = tk.Tk()
    app = LoginApp(login_window)
    login_window.mainloop()