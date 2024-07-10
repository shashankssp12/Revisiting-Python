'''
For smaller programs you can make the classes within the main class. 
On big scale project , you obviously import classes and their properties, attributes and methods as Module.
'''

class Car:
    # Constructor function
    def __init__(self):
        color = None
        model = None
        manufacturer = None
        
    def drive(self):
        print("This car is driving")

    def stop(self):
        print("The car has stopped")

# # What is "self" keyword ? 
'''
Gives reference of the current object. Also helpful in differntiating the Data Members(the class variables) from the method's local variables.
'''

## Additional:
'''
By convention, self is always the first parameter in a class method definition.
You can technically use a different name for self, but self is the standard practice for readability and consistency.
self is essential for creating object-oriented programs in Python, as it enables methods to work with object-specific data.
'''