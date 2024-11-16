#1 задание
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def width(self):
        return self._width

    def width(self, value):
        self._width = value

    def height(self):
        return self._height

    def height(self, value):
        self._height = value

    def area(self):
        return self.width * self.height


rect = Rectangle(10, 5)
rect.width = 15
print(rect.area())

#2 задание
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Название: '{self.title}', Автор: {self.author}, Год: {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

book = Book("Война и мир", "Лев Толстой", 1869)
print(book)
print(repr(book))


#3 задание
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def set_diameter(self, diameter):
        self.radius = diameter / 2


circle = Circle(5)
circle.set_diameter(10)
print(circle.area())


#4 задание
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    def balance(self):
        return self._balance

    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 <= amount <= self._balance:
            self._balance -= amount
        else:
            print("Ошибка: недостаточно средств или некорректная сумма")


account = BankAccount("12345678", 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)

#5 заданин
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def __len__(self):
        return len(self.books)


library = Library()
book1 = Book("Война и мир", "Лев Толстой", 1869)
library.add_book(book1)
print(len(library))


