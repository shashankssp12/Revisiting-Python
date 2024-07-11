'''
INHERITANCE - The child class has access to all the properties of the parent class and obviously have access to methods of itself.


'''

class Animals:
    alive = True

class Humans(Animals):
    def creates(self):
        print("This human can create")

class Dog(Animals):
    def bark(self):
        print("This dog barks")
        
        
dog1 = Dog()
print("Is this dog alive?",dog1.alive)
dog1.bark();

h1 = Humans()
print("Is this human alive?", h1.alive)
h1.creates();
