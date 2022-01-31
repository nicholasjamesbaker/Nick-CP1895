class Product:
    def __init__(self, name: str, price: float, discount_percent: float):
        print("init method is invoked")
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def getDiscountAmount(self):
        return self.price - self.getDiscountPrice()

    def getDiscountPrice(self):
        return (self.price * self.discount_percent) / 100

