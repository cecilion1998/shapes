from Point import Point


class Rectangle:
    def __init__(self, bottom_left, width, height):
        """Initialize the rectangle with the bottom-left corner point, width, and height."""
        self.bottom_left = bottom_left
        self.width = width
        self.height = height

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.bottom_left}, width={self.width}, height={self.height})"

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def move(self, dx, dy):
        """Move the rectangle by dx and dy."""
        self.bottom_left.move(dx, dy)

    def contains_point(self, point):
        """Check if the rectangle contains a given point."""
        return (self.bottom_left.x <= point.x <= self.bottom_left.x + self.width and
                self.bottom_left.y <= point.y <= self.bottom_left.y + self.height)

    def intersects(self, other):
        """Check if this rectangle intersects with another rectangle."""
        return not (self.bottom_left.x + self.width < other.bottom_left.x or
                    self.bottom_left.x > other.bottom_left.x + other.width or
                    self.bottom_left.y + self.height < other.bottom_left.y or
                    self.bottom_left.y > other.bottom_left.y + other.height)

    def top_right(self):
        """Get the top-right point of the rectangle."""
        return Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height)
