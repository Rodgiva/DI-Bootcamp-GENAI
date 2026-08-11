import math as m
class Circle():
    def __init__(self, radius:int = 0, diameter:int = 0):
        if radius == 0 and diameter == 0:
            raise ValueError("radius or diameter must be inputed")
        else:
            if radius == 0:
                self.diameter = diameter
                self.radius = diameter / 2
            elif diameter == 0:
                self.radius = radius
                self.diameter = radius*2

    @property
    def area(self)->int:
        return m.pi*2*self.radius

    def __str__(self):
        return f"Radius: {self.radius} Diameter: {self.diameter}"

    def __add__(self, other):
        return Circle(radius=(self.radius + other.radius))

    def __gt__(self, other):
        return True if self.radius > other.radius else False

    def __eq__(self, other):
        return True if self.radius == other.radius else False

    def __gt__(self, other):
        return True if self.radius < other.radius else False
    
circle = Circle(radius=5)
circle2 = Circle(radius=10)
print(circle.area)
print(circle)

circle3 = circle + circle2
print(circle3)
print(circle2 > circle)
print(circle > circle2)
print(circle2 == circle)

circle4 = Circle(radius=2)
circle5 = Circle(radius=20)

circles = [
    circle5,
    circle,
    circle2,
    circle4,
    circle3,
]

for circle in circles:
    print(circle)

def sort_circle(circles:list):
    for i in range(0, len(circles)):
        for j in range(0, len(circles)):
            while circles[j] < circles[i]:
                temp = circles[i]
                circles[i] = circles[j]
                circles[j] = temp
sort_circle(circles)
print("---")
for circle in circles:
    print(circle)