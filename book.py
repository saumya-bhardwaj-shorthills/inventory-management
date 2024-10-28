import json

class Book:
    def __init__(self, title: str, author: str, isbn: str, copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "copies": self.copies
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"], data["copies"])

    def add_copy(self, count: int = 1):
        self.copies += count

    def remove_copy(self, count: int = 1):
        if self.copies >= count:
            self.copies -= count
        else:
            raise ValueError("Insufficient copies to remove.")
