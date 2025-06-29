import math
from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        ...

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height
    
    def area(self):
        return self.width * self.height
    
class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self):
        return f"{(math.pi * (self.radius ** 2)):.2f}"
    
def calculate_area(shape: Shape) -> float:
    return shape.area()

if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    rectangle_area = calculate_area(rectangle)
    print("Rectangle area is: ", rectangle_area)

    circle = Circle(12)
    circle_area = calculate_area(circle)
    print(f"Circle area is: {circle_area}")