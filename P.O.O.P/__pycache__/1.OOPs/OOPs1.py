'''
For smaller programs you can make the classes within the main class. 
On big scale project , you obviously import classes and their properties, attributes and methods as Module.
'''

class Car:
    # class variable
    wheels = 4 #-------- This is a class variable , global variable, with it's default value 4 
    # now all objects , will have wheels attribute/property with 4 value , YES the value can definitely be updated.
    
    # Constructor --Speacial method
    def __init__(self,color,model,year):
        self.color = color #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        
    def drive(self):
        print("This {} is driving".format(self.model))

    def stop(self):
        print("This {} has stopped".format(self.model))

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