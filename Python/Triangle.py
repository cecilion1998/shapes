from Point import Point


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        """Initialize the triangle with three vertices."""
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

    def __repr__(self):
        """Return a string representation of the triangle."""
        return f"Triangle({self.vertex1}, {self.vertex2}, {self.vertex3})"

    def area(self):
        """Calculate the area of the triangle using the Shoelace formula."""
        return abs(
            self.vertex1.x * (self.vertex2.y - self.vertex3.y) +
            self.vertex2.x * (self.vertex3.y - self.vertex1.y) +
            self.vertex3.x * (self.vertex1.y - self.vertex2.y)
        ) / 2

    def perimeter(self):
        """Calculate the perimeter of the triangle."""
        return (
            self.vertex1.distance_to(self.vertex2) +
            self.vertex2.distance_to(self.vertex3) +
            self.vertex3.distance_to(self.vertex1)
        )

    def move(self, dx, dy):
        """Move the triangle by dx and dy."""
        self.vertex1.move(dx, dy)
        self.vertex2.move(dx, dy)
        self.vertex3.move(dx, dy)

    def contains_point(self, point):
        """Check if the triangle contains a given point using barycentric coordinates."""
        def sign(p1, p2, p3):
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

        d1 = sign(point, self.vertex1, self.vertex2)
        d2 = sign(point, self.vertex2, self.vertex3)
        d3 = sign(point, self.vertex3, self.vertex1)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)

    def centroid(self):
        """Calculate the centroid of the triangle."""
        x = (self.vertex1.x + self.vertex2.x + self.vertex3.x) / 3
        y = (self.vertex1.y + self.vertex2.y + self.vertex3.y) / 3
        return Point(x, y)
