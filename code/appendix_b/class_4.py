import numpy as np

class Circle:

    def __init__(self, radius):
        self.radius = radius

    # my first Instance method
    def description(self):
        return "circle with radius equal to {:.2f}".format(self.radius)

    # my secong instance method
    def area(self):
        return np.pi * self.radius ** 2
    
    # my secong instance method
    def circumference(self):
        return 2 * np.pi * self.radius
    
    # my tird instance method
    def diameter(self):
        return 2 * np.pi 
    

my_Circle = Circle(radius=2)

# Description
print(my_Circle.description())

# Calculate and report the area
my_Area = my_Circle.area()

# Reporting the area of my_Circle
print("The area of a {} is equal to {:.2f}".format(my_Circle.description(), my_Area)) 


    