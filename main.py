import tkinter as tk
from tkinter import messagebox

def submit_form():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    if username and password and email:
        messagebox.showinfo("Success", "Sign-up successful!")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Create the main window
root = tk.Tk()
root.title("Sign Up Form")

# Create a frame to hold the form elements
frame = tk.Frame(root)
frame.pack(expand=True, fill='both', padx=20, pady=20)

# Create and place the username label and entry
label_username = tk.Label(frame, text="Username:")
label_username.pack(anchor='center', pady=5)
entry_username = tk.Entry(frame)
entry_username.pack(anchor='center', pady=5)

# Create and place the password label and entry
label_password = tk.Label(frame, text="Password:")
label_password.pack(anchor='center', pady=5)
entry_password = tk.Entry(frame, show="*")
entry_password.pack(anchor='center', pady=5)

# Create and place the email label and entry
label_email = tk.Label(frame, text="Email:")
label_email.pack(anchor='center', pady=5)
entry_email = tk.Entry(frame)
entry_email.pack(anchor='center', pady=5)

# Create and place the submit button
button_submit = tk.Button(frame, text="Sign Up", command=submit_form)
button_submit.pack(anchor='center', pady=20)

# Run the application
root.mainloop()