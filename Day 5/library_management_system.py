import os
import json


DATA_FILE = os.path.join("Day 5", "library_data.json")


class Book:
    def __init__(self, title: str, author: str, id: str):
        self.title = title
        self.author = author
        self.id = id
        self.is_borrowed = False

   
    def to_dict(self):
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "id": self.id,
            "is_borrowed": self.is_borrowed,
        }

    
    @staticmethod
    def from_dict(data):
        if data.get("type") == "EBook":
            book = EBook(data["title"], data["author"], data["id"], data.get("file_size", "1MB"))
        else:
            book = Book(data["title"], data["author"], data["id"])
        book.is_borrowed = data.get("is_borrowed", False)
        return book

    def describe(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}"


# Inheritance: an EBook IS a Book, but with an extra detail (file size)
class EBook(Book):
    def __init__(self, title: str, author: str, id: str, file_size: str):
        super().__init__(title, author, id)  # reuse Book's setup
        self.file_size = file_size

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "EBook"
        data["file_size"] = self.file_size
        return data

    def describe(self):
        return super().describe() + f" [E-Book, {self.file_size}]"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("No books in the library yet.")
            return
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.describe()}, Status: {status}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, id):
        for book in self.books:
            if book.id == id and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'")
                return
        print("Book not available for borrowing or already borrowed.")

    def return_book(self, id):
        for book in self.books:
            if book.id == id and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'")
                return
        print("Book not found or was not borrowed.")


class LibraryManagementSystem:
    def __init__(self, json_file=DATA_FILE):
        self.library = Library()
        self.json_file = json_file

    # Read the file safely and rebuild real Book objects from dicts
    def load_books(self):
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
            self.library.books = [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.library.books = []

    # Save by turning every object back into a dict
    def save_books(self):
        with open(self.json_file, "w") as file:
            json.dump([book.to_dict() for book in self.library.books], file, indent=2)

    def run(self):
        self.load_books()

        while True:
            print("\nLibrary Management System")
            print("1. Add a new book")
            print("2. View all books")
            print("3. Search for a book")
            print("4. Borrow a book")
            print("5. Return a book")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                is_ebook = input("Is this an E-Book? (y/n): ").strip().lower()
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                book_id = input("Enter book ID: ").strip()

                if is_ebook == "y":
                    file_size = input("Enter file size (e.g., 5MB): ").strip()
                    new_book = EBook(title, author, book_id, file_size)
                else:
                    new_book = Book(title, author, book_id)

                self.library.add_book(new_book)
                self.save_books()
                print(f"Book '{title}' added successfully.")

            elif choice == "2":
                self.library.view_books()

            elif choice == "3":
                title = input("Enter book title to search: ").strip()
                found_book = self.library.search_book(title)
                if found_book:
                    status = "Borrowed" if found_book.is_borrowed else "Available"
                    print(f"Found Book - {found_book.describe()}, Status: {status}")
                else:
                    print("Book not found.")

            elif choice == "4":
                book_id = input("Enter book ID to borrow: ").strip()
                self.library.borrow_book(book_id)
                self.save_books()

            elif choice == "5":
                book_id = input("Enter book ID to return: ").strip()
                self.library.return_book(book_id)
                self.save_books()

            elif choice == "6":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    LibraryManagementSystem().run()
