class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def __str__(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    print('*', end="  ")
                else:
                    print(" ", end="  ")
            print()
        return ""

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.height * self.width


class Square(Rectangle):
    def __init__(self, length: int):
        Rectangle.__init__(self, length, length)


def main():
    print("Rectangle Calculator")
    keep_going = "y"
    while keep_going == "y":
        shape = input("\nRectangle or Square? (r/s): ")
        if shape == "r":
            height = int(input("Height:    "))
            width = int(input("Width:     "))
            rectangle = Rectangle(height, width)
            perimeter = rectangle.perimeter()
            area = rectangle.area()
            print("Perimeter:", perimeter)
            print("Area:     ", area)
            print(rectangle)
        elif shape == "s":
            length = int(input("Length:    "))
            square = Square(length)
            perimeter = square.perimeter()
            area = square.area()
            print("Perimeter:", perimeter)
            print("Area:     ", area)
            print(square)
        else:
            print("Incorrect letter entered")

        keep_going = input("Continue? (y/n): ")
        if keep_going == "n":
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
