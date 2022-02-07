from shapes import Circle, Rectangle
import pickle
import scene


def read():
    with open("shapes_list.bin", "rb") as file:
        shapes = pickle.load(file)
        return shapes


def write(shapes):
    with open("shapes_list.bin", "wb") as file:
        pickle.dump(shapes, file)


def main():
    """radius = float(input("Enter radius for circle: "))
    width = float(input("Enter width for rectangle: "))
    length = float(input("Enter length for rectangle: "))
    circle = Circle(radius, (3, 6))
    rectangle = Rectangle(length, width, (2, 4))
    shapes = [circle, rectangle]
    write(shapes)"""

    scene.add_shape(Circle(3, (3, 2)))


if __name__ == "__main__":
    main()
