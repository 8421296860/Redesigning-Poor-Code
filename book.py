from storage import FileStorage

file_storage = FileStorage()

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

def add_book(title, author, isbn):
    """
    Add a new book to the library.

    Args:
        title (str): Title of the book.
        author (str): Author of the book.
        isbn (str): ISBN of the book.

    Returns:
        bool: True if the book is successfully added, False otherwise.
    """
    # Check if the ISBN is already in use
    for existing_book in file_storage.load_books():
        if existing_book['isbn'] == isbn:
            print("Book with the same ISBN already exists.")
            return False

    # Create a new book instance
    new_book = Book(title, author, isbn)

    # Save the book to the storage
    file_storage.save_book(new_book)

    print("Book added successfully.")
    return True

def list_books():
    """
    List all books in the library.
    """
    books = file_storage.load_books()
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(book)
