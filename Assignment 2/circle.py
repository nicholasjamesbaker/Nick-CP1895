class Circle:
    def __init__(self, radius: float, color: str = "red"):
        self.__radius = radius
        self.__color = color
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
        self.__radius = r

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    def get_area(self):
        pi = 3.14
        area = pi * self.radius * self.radius
        return area

    def get_circumference(self):
        pi = 3.14
        circumference = 2 * pi * self.radius
        return circumference
