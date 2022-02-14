class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
