from point import Point
from line import Line
import math


class Rectangle:
    def __init__(self, bottom_left_corner: Point, top_right_corner: Point):
        self.__bottom_left_corner = bottom_left_corner
        self.__top_right_corner = top_right_corner
        assert isinstance(bottom_left_corner, Point), "Corner must be a point"
        assert isinstance(top_right_corner, Point), "Corner must be a point"

    @property
    def bottom_left_corner(self):
        return self.__bottom_left_corner

    @property
    def top_right_corner(self):
        return self.__top_right_corner

    @property
    def bottom_right_corner(self):
        point1 = self.__bottom_left_corner.y
        point2 = self.__top_right_corner.x
        new_point = Point(point2, point1)
        return new_point

    @property
    def top_left_corner(self):
        point1 = self.__bottom_left_corner.x
        point2 = self.__top_right_corner.y
        new_point = Point(point1, point2)
        return new_point

    @property
    def area(self):
        height = self.top_left_corner.y - self.bottom_right_corner.y
        width = self.bottom_right_corner.x - self.top_left_corner.x
        area = height * width
        return area

    @property
    def perimeter(self):
        height = self.top_left_corner.y - self.bottom_right_corner.y
        width = self.bottom_right_corner.x - self.top_left_corner.x
        perimeter = (height + width) * 2
        return perimeter
