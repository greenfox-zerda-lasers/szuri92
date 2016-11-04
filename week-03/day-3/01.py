# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area


class Circle():
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return self.radius * 2 * 3.14

    def get_area(self):
        return (self.radius ** 2) * 3.14


circle1 = Circle(10)

print(circle1.get_area())
print(circle1.get_circumference())
