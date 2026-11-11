import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    def describe(self):
        print(f"{self.__class__.__name__}: Area = {self.area():.2f}")
        
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2
    
class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
    
class Triangle(Shape):
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h


    
shapes = [Circle(7), Rectangle(5, 10), Triangle(6, 8)]

for s in shapes:
    s.describe()
