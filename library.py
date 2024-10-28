import json
from book import Book
from member import Member

class Library:
    def __init__(self, name: str, book_file='books.json', member_file='members.json', config_file='config.json'):
        self.name = name
        self.books = {}
        self.members = {}
        self.book_file = book_file
        self.member_file = member_file
        self.config_file = config_file
        self.next_user_id = 1  # Default starting user_id

        self.load_books()
        self.load_members()
        self.load_config()

    def load_config(self):
        """Load next_user_id from the config file."""
        try:
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                self.next_user_id = config.get("next_user_id", 1)
        except FileNotFoundError:
            print(f"{self.config_file} not found. Starting with user_id = 1.")

    def save_config(self):
        """Save the next_user_id to the config file."""
        with open(self.config_file, 'w') as file:
            json.dump({"next_user_id": self.next_user_id}, file, indent=4)

    def add_book(self, book: Book):
        self.books[book.isbn] = book
        self.save_books()

    def remove_book(self, book: Book):
        if book.isbn in self.books:
            del self.books[book.isbn]
            self.save_books()
        else:
            print("Book not found in library.")

    def add_member(self, name: str):
        member = Member(self.next_user_id, name)
        self.members[self.next_user_id] = member
        self.next_user_id += 1  # Increment user_id for the next member
        self.save_members()
        self.save_config()  # Save updated next_user_id to the config file
        print(f"Member '{name}' registered with user ID {member.user_id}.")

    def search_book(self, isbn: str):
        return self.books.get(isbn, None)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books.values():
                print(book)

    def save_books(self):
        with open(self.book_file, 'w') as file:
            json.dump({isbn: book.to_dict() for isbn, book in self.books.items()}, file, indent=4)

    def load_books(self):
        try:
            with open(self.book_file, 'r') as file:
                data = json.load(file)
                self.books = {isbn: Book.from_dict(book_data) for isbn, book_data in data.items()}
        except FileNotFoundError:
            print(f"{self.book_file} not found. Starting with an empty library.")

    def save_members(self):
        with open(self.member_file, 'w') as file:
            json.dump({user_id: member.to_dict() for user_id, member in self.members.items()}, file, indent=4)

    def load_members(self):
        try:
            with open(self.member_file, 'r') as file:
                data = json.load(file)
                self.members = {int(user_id): Member.from_dict(member_data, self) for user_id, member_data in data.items()}
        except FileNotFoundError:
            print(f"{self.member_file} not found. Starting with no members.")
