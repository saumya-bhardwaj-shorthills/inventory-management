
---
# Library Management System

A simple and modular Library Management System implemented in Python, following Object-Oriented Design principles. This system allows users to add, remove, and search for books, register members, borrow and return books, and display all available books. All data is stored persistently in JSON files, making it accessible across program runs.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Examples](#examples)
- [Dependencies](#dependencies)

---

## Features

- **Book Management**: Add, remove, display, and search for books by ISBN.
- **Member Registration**: Register new members with a self-incremental user ID.
- **Borrowing and Returning Books**: Members can borrow available books and return them after use.
- **Persistent Storage**: All data is stored in JSON files to ensure persistence.
- **Modular Design**: Follows a strict Object-Oriented Design with separate modules for books, members, and library operations.

## Project Structure

```
├── library.py         # Contains Library class and core operations
├── book.py            # Contains Book class to define book-related properties
├── member.py          # Contains Member class to define member properties and borrowing logic
├── main.py            # Main file to run the Library Management System
├── books.json         # JSON file to store book data
├── members.json       # JSON file to store member data
├── config.json        # JSON file to store incremental user_id configuration
└── README.md          # Project documentation
```

### Class Overview

- **Library**: Manages books, members, and handles saving/loading data.
- **Book**: Defines properties of a book and tracks available copies.
- **Member**: Defines member details, borrowed books, and handles borrowing/returning logic.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. **Install Dependencies**: There are no external dependencies, as it only requires Python 3.x.

3. **Run the Program**:
   ```bash
   python main.py
   ```

## Usage

When you run the program, you will be presented with the main menu:

```
--- Library Management System ---
1. Add a book
2. Remove a book
3. Display all books
4. Register a member
5. Borrow a book
6. Return a book
7. View member's borrowed books
8. Exit
```

Follow the prompts to perform various operations.

### Examples

1. **Adding a Book**
   - Enter details like title, author, ISBN, and the number of copies.
   
2. **Registering a Member**
   - Enter the name of the member to register. The system assigns a unique, self-incrementing `user_id`.
   
3. **Borrowing a Book**
   - Enter the `user_id` of the member and the `ISBN` of the book they wish to borrow. If available, the book is marked as borrowed.

4. **Returning a Book**
   - Enter the `user_id` of the member and the `ISBN` of the book they wish to return. The book is marked as returned.

5. **Viewing Borrowed Books**
   - Enter the `user_id` to see the list of books currently borrowed by the member.

## Dependencies

- **Python 3.x**: This system is built using Python and does not require additional libraries.


