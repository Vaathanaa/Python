#exercise 1
class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Animal Name: {self.name}")
        print(f"Animal age: {self.age}")
a1 = Animal("Leo",4)
a1.show_info()
#exercise 2
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print("Car details:")
        print(f"  Make : {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Year : {self.year}")
        
C = Car('toyota', 'corola', 2007)
C.display_info()
#exercise 3
class Car:
    def __init__(self,year):
        self.year = year
    def is_vintage(self,carNumber):
        if self.year > 25:
            print(f"Car {carNumber} is vintage : True")
        else:
            print(f"Car {carNumber} is vintage : False")
C1 = Car(23)
C1.is_vintage(1)
C2 = Car(67)
C2.is_vintage(2)
#exercise 4
class Student():
    def __init__(self,name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    def update_grade(self,new_grade):
        print("before update")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"grade = {self.grade}")
        
        self.grade = new_grade
        print("After update")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"grade = {self.grade}")        
S1=Student('vathana', 18, 'B')
S1.update_grade('A')
#exercise 5
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        print(f"Depositing ${amount}")
        self.balance += amount
        print(f"New balance: ${self.balance}")

    def withdraw(self, amount):
        print(f"Withdrawing ${amount}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance: ${self.balance}")
        else:
            print(f"Attempting to withdraw ${amount}")
            print("Insufficient funds. Withdrawal failed.")
account = BankAccount("Vathana", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
#exercise 6
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
#exercise 7
class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
    def add_student(self, name):
        print(f"Added student: {name}")
        self.students.append(name)
    def list_students(self):
        print(f"Students in {self.class_name}:")
        for student in self.students:
            print(f" {student}")
room = Classroom("Math 101")
room.add_student("Alice")
room.add_student("Bob")
room.add_student("Charlie")
room.list_students()
#exercise 8
class PhoneBook:
    def __init__(self):
        self.contacts = {} 
    def add_contact(self, name, number):
        print(f"Added contact: {name} -> {number}")
        self.contacts[name] = number
    def find_contact(self, name):
        if name in self.contacts:
            print(f"{name}'s number: {self.contacts[name]}")
        else:
            print(f"{name} can't found in phone book.")
pb = PhoneBook()
pb.add_contact("John", "+855811314573")
pb.add_contact("Jane", "+855826481946")
pb.find_contact("John")
pb.find_contact("Alice")
pb.find_contact("Jane")