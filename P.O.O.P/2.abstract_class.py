'''
Abstract Class - A class that has one or more abstract methods. No objects, can be created out of an abstract class.
Abstract Methods - An abstract method is a method , that is being defined but cannot be ustilized.(A ghost method).This compels the user to override the method by a child class.

Why Use Them?

-Enforces a common interface for child classes.
-Ensures child classes implement essential functionality.
'''

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class for shapes
    @abstractmethod
    def area(self):
        pass  # Abstract method - child classes must implement it

class Circle(Shape):  # Concrete subclass (inherits from Shape)
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Overriding the abstract method
        return 3.14 * self.radius**2

# We cannot create a Shape object directly (abstract class)
# shape = Shape()  # This will cause an error

# Create a Circle object (concrete subclass)
circle = Circle(5)
print(circle.area())  # Output: 78.5

