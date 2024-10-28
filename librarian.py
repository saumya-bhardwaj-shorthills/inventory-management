from user import User
from book import Book


class Librarian(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)

    def add_book(self, library, book: Book):
        library.add_book(book)
        print(f"Librarian {self.name} added {book.title} to the library.")

    def remove_book(self, library, book: Book):
        library.remove_book(book)
        print(f"Librarian {self.name} removed {book.title} from the library.")
