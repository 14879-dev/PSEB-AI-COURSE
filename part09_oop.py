
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 10-11-2026

# PART 9: OOP - CLASSES AND OBJECTS


# ==========================================
# WARM-UP: STUDENT CLASS
# ==========================================

class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"


print("\n========== WARM-UP: STUDENT CLASS ==========")

student1 = Student("Ali", 12, [80, 85, 78])
student2 = Student("Sara", 15, [90, 85, 88])

student1.add_mark(81)

print(student1)
print(student2)


# ==========================================
# BUILD: BANK ACCOUNT
# ==========================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        self.history.append(f"Deposited: Rs. {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        self.history.append(f"Withdrawn: Rs. {amount}")

    def show_history(self):
        print("\nTransaction History:")

        for transaction in self.history:
            print(transaction)

        print("Current Balance: Rs.", self.balance)


print("\n========== BUILD: BANK ACCOUNT ==========")

account1 = BankAccount("Mudassir", 5000)

account1.deposit(2000)
account1.withdraw(1500)

# Testing invalid transactions

try:
    account1.withdraw(10000)
except ValueError as error:
    print("Transaction Error:", error)

try:
    account1.deposit(-500)
except ValueError as error:
    print("Transaction Error:", error)

print("\nAccount Owner:", account1.owner)
account1.show_history()


# ==========================================
# CHALLENGE: LIBRARY SYSTEM
# ==========================================

# BOOK CLASS

class Book:

    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


# LIBRARY CLASS

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed: {title}")
                return

        print(f"{title} is not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You returned: {title}")
                return

        print(f"{title} cannot be returned")

    def available_books(self):
        print("\nAvailable Books:")

        for book in self.books:
            if book.available:
                print(book)


# EBOOK CLASS: INHERITANCE

class EBook(Book):

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} - {self.file_size} MB"


print("\n========== CHALLENGE: LIBRARY SYSTEM ==========")

# Creating library object

library = Library()

# Creating book objects

book1 = Book("Python Basics", "John Smith")
book2 = Book("Machine Learning", "Andrew Ng")

ebook1 = EBook("Deep Learning", "Ian Goodfellow", 25)

# Adding books to library

library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)

# Displaying available books

library.available_books()

# Borrowing a book

library.borrow("Python Basics")

# Returning a book

library.return_book("Python Basics")

# Displaying available books again

library.available_books()

# Displaying EBook information

print("\nEBook Information:")
print(ebook1)


print("\n========== PART 9 COMPLETED ==========")
