from point import Point
from line import Line
import math


class Rectangle:
    def __init__(self, bottom_left_corner: Point, top_right_corner: Point):
        self.__bottom_left_corner = bottom_left_corner
        self.__top_right_corner = top_right_corner
        assert bottom_left_corner != Point, "must have point perimeter"
        assert top_right_corner != Point, "must have point perimeter"

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
        new_point = Point(point1, point2)
        return new_point

    @property
    def top_left_corner(self):
        point1 = self.__bottom_left_corner.x
        point2 = self.__top_right_corner.y
        new_point = Point(point1, point2)
        return new_point

    @property
    def area(self):
        line1 = Line(self.bottom_left_corner, self.bottom_right_corner)
        line2 = Line(self.top_left_corner, self.top_right_corner)
        length1 = line1.length
        length2 = line2.length
        area = length1 * length2
        return area

    @property
    def perimeter(self):
        line1 = Line(self.bottom_left_corner, self.bottom_right_corner)
        line2 = Line(self.top_left_corner, self.top_right_corner)
        length1 = line1.length
        length2 = line2.length
        perimeter = 2 * (length1 + length2)
        return perimeter
