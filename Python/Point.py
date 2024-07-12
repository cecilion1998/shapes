class Point:
    def __init__(self, x=0, y=0):
        """Initialize the point with optional x and y coordinates."""
        self.x = x
        self.y = y

    def __repr__(self):
        """Return a string representation of the point."""
        return f"Point({self.x}, {self.y})"

    def distance_to_origin(self):
        """Calculate the distance from the point to the origin (0, 0)."""
        return (self.x**2 + self.y**2)**0.5

    def distance_to(self, other):
        """Calculate the distance between this point and another point."""
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def move(self, dx, dy):
        """Move the point by dx and dy."""
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        """Check if two points are equal."""
        return self.x == other.x and self.y == other.y