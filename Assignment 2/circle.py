from math import pi
class Circle:
    def __init__(self, radius: float, color: str = "red"):
        self.__radius = radius
        self.__color = color
        assert isinstance(radius, float), "Radius must be a float"
        assert radius > 0, "Radius must be greater than zero"


    def __str__(self):
        return f"The radius of the circle is {self.radius}."

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, r):
        if r <= 0:
            raise ValueError("Number must be greater than zero.")
        if not isinstance(r, float):
            raise TypeError("Input must be a float")
        self.__radius = r

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    def get_area(self):
        area = pi * self.radius * self.radius
        return area

    def get_circumference(self):
        circumference = 2 * pi * self.radius
        return circumference
