class Circle:
    def __init__(self, center, radius):
        """Initialize the circle with a center point and radius."""
        self.center = center
        self.radius = radius

    def __repr__(self):
        """Return a string representation of the circle."""
        return f"Circle({self.center}, radius={self.radius})"

    def area(self):
        """Calculate the area of the circle."""
        return 3.141592653589793 * self.radius ** 2

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * 3.141592653589793 * self.radius

    def move(self, dx, dy):
        """Move the circle by dx and dy."""
        self.center.move(dx, dy)

    def contains_point(self, point):
        """Check if the circle contains a given point."""
        return self.center.distance_to(point) <= self.radius

    def distance_to(self, other):
        """Calculate the distance between the center of this circle and another circle."""
        return self.center.distance_to(other.center) - (self.radius + other.radius)