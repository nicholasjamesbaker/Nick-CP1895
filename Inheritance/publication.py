class Publication:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, period: str, publisher: str, title: str, price: float):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, author: str, pages: int, title: str, price: float):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Newspaper(Periodical):
    def __init__(self, publisher: str, title: str, price: float, period: str):
        super().__init__(period, publisher, title, price)


class Magazine(Periodical):
    def __init__(self, publisher: str, title: str, price: float, period: str):
        super().__init__(period, publisher, title, price)


b1 = Book("Aldous Huxley", 311, "Brave New World", 29.0)
n1 = Newspaper("New York Times Company", "NY Times", 6, "Daily")
m1 = Magazine("Springer Nature", "Scientific American", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
