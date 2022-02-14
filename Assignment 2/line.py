from point import Point
import math


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.__start_point = start_point
        self.__end_point = end_point
        assert start_point != Point, "must have point perimeter"
        assert end_point != Point, "must have point perimeter"

    @property
    def start_point(self):
        return self.__start_point

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, e):
        self.__end_point = e

    @property
    def length(self):
        distance = ((((self.__end_point.x - self.__start_point.x) ** 2) + ((self.__end_point.y - self.__start_point.y) ** 2)) ** 0.5)
        return distance

