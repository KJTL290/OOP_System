from tkinter import *

root = Tk()
root.title("Radio Button")

# Define the variable to hold the state of the radiobuttons
r = IntVar()

def update_label():
    my_label.config(text=r.get())

Radiobutton(root, text="Option 1", variable=r, value=1, command=update_label).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=update_label).pack()

my_label = Label(root, text=r.get())
my_label.pack()

root.mainloop()