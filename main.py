import tkinter as tk
from tkinter import messagebox

def login_action():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    if username and password and email:
        messagebox.showinfo("Log in Succesfully.", "Thank you for Choosing Our website.")
    else:
        messagebox.showerror("Error.", "Please Fill up the Form.")

root = tk.Tk()
root.title("Log In Form")



label_username = tk.Label(root, text="Username")
label_username.pack()
entry_username = tk.Entry(root, width=40)
entry_username.pack()

label_password = tk.Label(root, text="Password")
label_password.pack()
entry_password = tk.Entry(root, show="*", width=40)
entry_password.pack()

label_email = tk.Label(root, text="Email/Gmail")
label_email.pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()
login_button = tk.Button(root, text="Log In", command=login_action)
login_button.pack()

root.mainloop()