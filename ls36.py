class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, color, width, height):
        Shape.__init__(self, color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle("Red", 5)
print("Color: ", circle.color, " Radius: ", circle.radius, " Area: ", circle.area())

rectangle = Rectangle("Blue", 4, 6)
print("Color: ", rectangle.color, " Width: ", rectangle.width, " Height: ", rectangle.height, " Area: ", rectangle.area())
