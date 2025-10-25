
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not_filled'}")
  
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with area of {3.14* self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"It is a square with and area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"It is a triangle with and area of {(self.width * self.height) / 2}cm^2")

circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=6)
triangle = Triangle(color="yellow", filled=True, width = 7, height = 8)


triangle.describe()


# print(circle.color)
# print(circle.filled)
# print(circle.radius)
# print(triangle.color)
# print(triangle.filled)
# print(triangle.width)
# print(triangle.height)
