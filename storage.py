import json

class FileStorage:
    def __init__(self):
        self.books_file = 'books.json'
        self.users_file = 'users.json'
        self.checkouts_file = 'checkouts.json'

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self, data, file_name):
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def load_books(self):
        return self.load_data(self.books_file)

    def save_book(self, book):
        books = self.load_books()
        books.append(book.__dict__)
        self.save_data(books, self.books_file)

    def load_users(self):
        return self.load_data(self.users_file)

    def save_user(self, name, user_id):
        users = self.load_users()
        users.append({"name": name, "user_id": user_id})
        self.save_data(users, self.users_file)

    def load_checkouts(self):
        return self.load_data(self.checkouts_file)

    def save_checkouts(self, checkouts):
        self.save_data(checkouts, self.checkouts_file)

    def add_checkout(self, user_id, isbn):
        checkouts = self.load_checkouts()
        checkouts.append({"user_id": user_id, "isbn": isbn})
        self.save_checkouts(checkouts)

    def update_book_availability(self, isbn, available):
        books = self.load_books()
        for book in books:
            if book['isbn'] == isbn:
                book['available'] = available
                self.save_data(books, self.books_file)
                break
