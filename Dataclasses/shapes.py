from dataclasses import dataclass


class Circle:
    radius: float
    center_position: tuple

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_circumference(self):
        return 2 * 3.14 * self.radius


class Rectangle:
    length: float
    width: float
    top_left_corner_position: tuple

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)
