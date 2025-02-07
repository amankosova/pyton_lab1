class Shape:
    def __init__(self):
        self.area_value = 0

    def area(self):
        print(f"Area of the shape: {self.area_value}")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        area_value = self.length * self.width
        print(f"Area of the rectangle: {area_value}")

shape = Shape()
shape.area()

rectangle = Rectangle(5, 3)
rectangle.area()
