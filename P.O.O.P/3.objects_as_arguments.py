'''
The object of a class can be passed as an argument, as long as the object has some attribute function(in which the arg is pass) has something to do with it.
'''

'''
The method assign_color is a seperate function and is not the child of the Car or any other class
'''

class Car:
    color = None

class Bag:
    color = None
    
    
def assign_color(object,colour):
    object.color = colour

# Both the Bag and the Car class have this attribute color.

c1 = Car()
assign_color(c1,"Red")
print(c1.color)

bag = Bag()
assign_color(bag,"Black")
print(bag.color)
