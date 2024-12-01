import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Log In Form")

label = tk.Label(root, text="Username")
label.pack()

label2 = tk.Label(root, text="Password")
label2.pack()

label3 = tk.Label(root, text="Email/Gmail")
label3.pack()

label4 = tk.Label(root, text="Log In")
label4.pack()

root.mainloop()
