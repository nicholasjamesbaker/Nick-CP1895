from dataclasses import dataclass


@dataclass
class Product:
    __price: float
    name: str
    discountPercent: float

    def get_price(self):
        return self.__price

    def get_discount_amount(self):
        return self.__price * self.discountPercent

    def get_discount_price(self):
        discount_amount = self.__price * self.discountPercent
        return self.__price - discount_amount
