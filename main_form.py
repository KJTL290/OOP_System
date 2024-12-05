import tkinter as tk

def open_main_form():
    # Create the main form window
    main_window = tk.Tk()
    main_window.title("Main Form")

    # Add some content to the main form
    tk.Label(main_window, text="Welcome to the Main Form!").pack()

    main_window.mainloop()