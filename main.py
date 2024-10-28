from book import Book
from member import Member
from library import Library

def display_menu():
    print("\n--- Library Management System ---")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display all books")
    print("4. Register a member")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. View member's borrowed books")
    print("8. Exit")
    print("---------------------------------")

def main():
    library = Library("City Library")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a book
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, isbn, copies)
            library.add_book(book)
            print(f"Book '{title}' added successfully.")

        elif choice == "2":
            # Remove a book
            isbn = input("Enter ISBN of the book to remove: ")
            book = library.search_book(isbn)
            if book:
                library.remove_book(book)
                print(f"Book '{book.title}' removed successfully.")
            else:
                print("Book not found.")

        elif choice == "3":
            # Display all books
            print("\nAvailable books in the library:")
            library.display_books()

        elif choice == "4":
            # Register a member
            name = input("Enter member name: ")
            library.add_member(name)

        elif choice == "5":
            # Borrow a book
            user_id = int(input("Enter member ID: "))
            member = library.members.get(user_id)
            if member:
                isbn = input("Enter ISBN of the book to borrow: ")
                book = library.search_book(isbn)
                if book:
                    member.borrow_book(book)
                    library.save_books()  # Save updated book data
                    library.save_members()  # Save updated member data
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == "6":
            # Return a book
            user_id = int(input("Enter member ID: "))
            member = library.members.get(user_id)
            if member:
                isbn = input("Enter ISBN of the book to return: ")
                book = library.search_book(isbn)
                if book:
                    member.return_book(book)
                    library.save_books()  # Save updated book data
                    library.save_members()  # Save updated member data
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == "7":
            # View member's borrowed books
            user_id = int(input("Enter member ID: "))
            member = library.members.get(user_id)
            if member:
                if member.borrowed_books:
                    print(f"\nBooks borrowed by {member.name}:")
                    for book in member.borrowed_books:
                        print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")
                else:
                    print(f"{member.name} has not borrowed any books.")
            else:
                print("Member not found.")

        elif choice == "8":
            # Exit
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
