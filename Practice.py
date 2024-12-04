import tkinter as tk
from tkinter import ttk

# Initialize the root window
root = tk.Tk()
root.title("Combobox widget")
root.geometry("300x200")

# Define the callback function for selection
def on_selection(event):
    selected_item = combo.get()
    print("You selected", selected_item)

# Create the Combobox widget
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3", "Option 4"])
combo.set("Select an Option")

# Bind the selection event
combo.bind("<<ComboboxSelected>>", on_selection)
combo.pack(pady=20)

# Start the main event loop
root.mainloop()