class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    
shape = Shape()
print("Area of Shape:", shape.area())

square = Square(4)
print("Area of Square:", square.area())
