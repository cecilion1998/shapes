# shape_manager.py
from Point import Point
from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle
from Square import Square


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def create_point(self):
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        point = Point(x, y)
        self.shapes.append(point)
        print(f"Created {point}")
        return point

    def create_circle(self):
        print("Creating center point for the circle:")
        center = self.create_point()
        radius = float(input("Enter radius: "))
        circle = Circle(center, radius)
        self.shapes.append(circle)
        print(f"Created {circle}")
        return circle

    def create_rectangle(self):
        print("Creating bottom-left corner point for the rectangle:")
        bottom_left = self.create_point()
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        rectangle = Rectangle(bottom_left, width, height)
        self.shapes.append(rectangle)
        print(f"Created {rectangle}")
        return rectangle

    def create_square(self):
        print("Creating bottom-left corner point for the square:")
        bottom_left = self.create_point()
        side_length = float(input("Enter side length: "))
        square = Square(bottom_left, side_length)
        self.shapes.append(square)
        print(f"Created {square}")
        return square

    def create_triangle(self):
        print("Creating first vertex of the triangle:")
        vertex1 = self.create_point()
        print("Creating second vertex of the triangle:")
        vertex2 = self.create_point()
        print("Creating third vertex of the triangle:")
        vertex3 = self.create_point()
        triangle = Triangle(vertex1, vertex2, vertex3)
        self.shapes.append(triangle)
        print(f"Created {triangle}")
        return triangle

    def select_shape(self):
        print("Select shape type to create:")
        print("1. Point")
        print("2. Circle")
        print("3. Rectangle")
        print("4. Square")
        print("5. Triangle")
        choice = int(input("Enter choice: "))

        if choice == 1:
            return self.create_point()
        elif choice == 2:
            return self.create_circle()
        elif choice == 3:
            return self.create_rectangle()
        elif choice == 4:
            return self.create_square()
        elif choice == 5:
            return self.create_triangle()
        else:
            print("Invalid choice!")
            return None

    def use_shape_function(self, shape):
        if isinstance(shape, Circle):
            print("1. Area")
            print("2. Circumference")
            choice = int(input("Enter function to use: "))
            if choice == 1:
                print(f"Area: {shape.area()}")
            elif choice == 2:
                print(f"Circumference: {shape.circumference()}")
            else:
                print("Invalid choice!")

        elif isinstance(shape, Rectangle):
            print("1. Area")
            print("2. Perimeter")
            choice = int(input("Enter function to use: "))
            if choice == 1:
                print(f"Area: {shape.area()}")
            elif choice == 2:
                print(f"Perimeter: {shape.perimeter()}")
            else:
                print("Invalid choice!")

        elif isinstance(shape, Square):
            print("1. Area")
            print("2. Perimeter")
            choice = int(input("Enter function to use: "))
            if choice == 1:
                print(f"Area: {shape.area()}")
            elif choice == 2:
                print(f"Perimeter: {shape.perimeter()}")
            else:
                print("Invalid choice!")

        elif isinstance(shape, Triangle):
            print("1. Area")
            print("2. Perimeter")
            print("3. Centroid")
            choice = int(input("Enter function to use: "))
            if choice == 1:
                print(f"Area: {shape.area()}")
            elif choice == 2:
                print(f"Perimeter: {shape.perimeter()}")
            elif choice == 3:
                print(f"Centroid: {shape.centroid()}")
            else:
                print("Invalid choice!")

        elif isinstance(shape, Point):
            print(f"Point coordinates: ({shape.x}, {shape.y})")

        else:
            print("Unknown shape type!")

def main():
    manager = ShapeManager()
    while True:
        print("1. Create Shape")
        print("2. Use Shape Function")
        print("3. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            manager.select_shape()
        elif choice == 2:
            if not manager.shapes:
                print("No shapes available. Create a shape first.")
                continue
            print("Select a shape to use its function:")
            for i, shape in enumerate(manager.shapes):
                print(f"{i + 1}. {shape}")
            shape_index = int(input("Enter shape number: ")) - 1
            if 0 <= shape_index < len(manager.shapes):
                manager.use_shape_function(manager.shapes[shape_index])
            else:
                print("Invalid shape number!")
        elif choice == 3:
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
