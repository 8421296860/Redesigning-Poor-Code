class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
