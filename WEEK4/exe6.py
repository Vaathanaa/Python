class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def show_books(self):
        print("Books in the library:")
        for i in range(len(self.books)):
            book = self.books[i]
            print(f"{i+1}. Title: {book.title}, Author: {book.author}, Price: ${book.price}")
lib = Library()
lib.add_book(Book("The Great Man", "Vathana", 284.45))
lib.add_book(Book("The Darkside", "Vathana", 9999))
lib.add_book(Book("1984", "John wick", 100000))
lib.show_books()
        
        