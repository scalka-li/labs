# task 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"название: {self.title}, автор: {self.author}, год: {self.year}"


book1 = Book("ляляля", "бла блабла", 2025)
print(book1.get_info())


# task 2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get(self):
        return self.radius

    def set(self, new):
        self.radius = new


circle = Circle(1)
circle.set(2)
print(circle.get())
