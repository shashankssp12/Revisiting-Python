'''
Think of it as a bridge: It connects a child class to its parent class.
Calling parent methods: Use super() to call methods defined in the parent class from a child class method.
Overrides without forgetting: When overriding a method, super() lets you call the parent's version even after making changes in the child.
Remember, super() doesn't create objects, it just helps you call methods across classes.
'''

# use case


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        print("Area is:")
        return self.length*self.width

class Cube(Square):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        volume = self.length*self.height*self.width
        print("Volume is ",end=": ")
        return volume

square = Square(5,6)
print(square.area())

myCube = Cube(12,12,12)
print(myCube.volume())