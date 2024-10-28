from user import User
from book import Book

class Member(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self.borrowed_books = []

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "borrowed_books": [book.isbn for book in self.borrowed_books]
        }

    @classmethod
    def from_dict(cls, data, library):
        member = cls(data["user_id"], data["name"])
        member.borrowed_books = [library.books[isbn] for isbn in data["borrowed_books"] if isbn in library.books]
        return member

    def borrow_book(self, book: Book):
        if book.copies > 0:
            book.remove_copy()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is currently unavailable.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.add_copy()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")
