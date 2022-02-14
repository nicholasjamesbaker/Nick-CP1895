class Publication:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price


class Book(Publication):
    def __init__(self, author: str, pages: int, title: str, price: float):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Newspaper(Publication):
    def __init__(self, publisher: str, pages: int, title: str, price: float):
        super().__init__(title, price)
        self.publisher = publisher
        self.pages = pages


class Magazine(Publication):
    def __init__(self, publisher: str, pages: int, title: str, price: float):
        super().__init__(title, price)
        self.publisher = publisher
        self.pages = pages


b1 = Book("Aldous Huxley", 311, "Brave New World", 29.0)
n1 = Newspaper("New York Times Company", 10, "NY Times", 6.0)
m1 = Magazine("Springer Nature", 40, "Scientific American", 5.99)

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
