"""9"""


class Circle:
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.pi * self.radius


circle_one = Circle(30)
print(circle_one.area())
print(circle_one.perimeter())
