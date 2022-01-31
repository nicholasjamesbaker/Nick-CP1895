class Product:
    def __init__(self, name: str, price: float, discount_percent: float):
        print("init method is invoked")
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def getDiscountAmount(self):
        return self.price / self.discount_percent

    def getDiscountPrice(self):
        discount_amount = self.price / self.discount_percent
        return self.price + discount_amount

