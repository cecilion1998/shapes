class Square:
    def __init__(self, bottom_left, side_length):
        """Initialize the square with the bottom-left corner point and side length."""
        self.bottom_left = bottom_left
        self.side_length = side_length

    def __repr__(self):
        """Return a string representation of the square."""
        return f"Square({self.bottom_left}, side_length={self.side_length})"

    def area(self):
        """Calculate the area of the square."""
        return self.side_length ** 2

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.side_length

    def move(self, dx, dy):
        """Move the square by dx and dy."""
        self.bottom_left.move(dx, dy)

    def contains_point(self, point):
        """Check if the square contains a given point."""
        return (self.bottom_left.x <= point.x <= self.bottom_left.x + self.side_length and
                self.bottom_left.y <= point.y <= self.bottom_left.y + self.side_length)
