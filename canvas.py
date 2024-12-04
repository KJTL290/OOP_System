import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Canvas Example")

    # Create a Canvas widget
    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Draw a line
    canvas.create_line(10, 10, 200, 200, fill='blue', width=2)

    # Draw a rectangle
    canvas.create_rectangle(50, 50, 150, 100, fill='red')

    # Draw an oval
    canvas.create_oval(200, 50, 300, 150, fill='green')

    # Add text
    canvas.create_text(200, 250, text="Hello, Canvas!", font=('Arial', 16))

    # Display an image (assuming you have a 'sample.png' in the same directory)
    # image = tk.PhotoImage(file='sample.png')
    # canvas.create_image(200, 150, image=image)

    root.mainloop()

if __name__ == "__main__":
    main()