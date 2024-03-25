from storage import FileStorage

file_storage = FileStorage()

def checkout_book(user_id, isbn):
    """
    Checkout a book from the library.

    Args:
        user_id (str): User ID of the borrower.
        isbn (str): ISBN of the book to checkout.

    Returns:
        bool: True if the checkout is successful, False otherwise.
    """
    # Check if the book is available
    for book in file_storage.load_books():
        if book['isbn'] == isbn:
            if book['available']:
                # Add checkout record
                file_storage.add_checkout(user_id, isbn)
                # Update book availability
                file_storage.update_book_availability(isbn, False)
                print("Book checked out successfully.")
                return True
            else:
                print("Book is already checked out.")
                return False

    print("Book not found.")
    return False
