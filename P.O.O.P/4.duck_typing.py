'''
Duck typing : it is the concept where the object of class is less important than the methods/attributes. Class type is not checked if the minimum methods/attributes are present.

the calling method assumes: 
"If it walks like a duck, and talks like a duck, then it must be a duck"

'''

class Duck:
    def walk(self):
        print("This duck can walk")
    def talk(self):
        print("This duck can talk")

class Chicken:
    def walk(self):
            print("This Chicken can walk")
    def talk(self):
            print("This Chicken can talk")

class Rabbit:
    def hops(self):
        print("This rabbit hops")
    def talk(self):
        print("Rabbits cannot talk")
        

class Person:
    def catch(self,object_animal):
        object_animal.walk()
        object_animal.talk()
        print("Caught")
        
duck = Duck()
chicken = Chicken()
rabbit = Rabbit()

p1 = Person()
p1.catch(duck)
p1.catch(chicken)
p1.catch(rabbit) ### AttributeError: 'Rabbit' object has no attribute 'walk'.