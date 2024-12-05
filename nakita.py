import tkinter as tk
from tkinter import messagebox, simpledialog

class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        
        self.users = []  # List to store user data
        self.books = []  # List to store book data
        self.current_user = None
        
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Login", font=("Arial", 24)).pack(pady=20)
        
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        
        tk.Label(self.root, text="Email:").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)
        
        tk.Button(self.root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        
        if username and email:
            self.current_user = {'username': username, 'email': email}
            self.main_form()
        else:
            messagebox.showerror("Error", "Please enter both username and email.")

    def main_form(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Library Management System", font=("Arial", 24)).pack(pady=20)
        
        tk.Button(self.root, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=10)
        tk.Button(self.root, text="Update Book", command=self.update_book).pack(pady=10)
        tk.Button(self.root, text="View Books", command=self.view_books).pack(pady=10)
        tk.Button(self.root, text="Delete Book", command=self.delete_book).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    def register(self):
        username = simpledialog.askstring("Register", "Enter username:")
        email = simpledialog.askstring("Register", "Enter email:")
        
        if username and email:
            self.users.append({'username': username, 'email': email})
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "Please enter both username and email.")

    def add_book(self):
        book_title = simpledialog.askstring("Add Book", "Enter book title:")
        if book_title:
            self.books.append(book_title)
            messagebox.showinfo("Success", f"Book '{book_title}' added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a book title.")

    def update_book(self):
        book_title = simpledialog.askstring("Update Book", "Enter book title to update:")
        if book_title in self.books:
            new_title = simpledialog.askstring("Update Book", "Enter new book title:")
            if new_title:
                index = self.books.index(book_title)
                self.books[index] = new_title
                messagebox.showinfo("Success", f"Book '{book_title}' updated to '{new_title}'!")
            else:
                messagebox.showerror("Error", "Please enter a new book title.")
        else:
            messagebox.showerror("Error", "Book title not found.")

    def view_books(self):
        if self.books:
            books_list = "\n".join(self.books)
            messagebox.showinfo("View Books", f"Books:\n{books_list}")
        else:
            messagebox.showinfo("View Books", "No books available.")

    def delete_book(self):
        book_title = simpledialog.askstring("Delete Book", "Enter book title to delete:")
        if book_title in self.books:
            self.books.remove(book_title)
            messagebox.showinfo("Success", f"Book '{book_title}' deleted successfully!")
        else:
            messagebox.showerror("Error", "Book title not found.")

    def logout(self):
        self.current_user = None
        self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()