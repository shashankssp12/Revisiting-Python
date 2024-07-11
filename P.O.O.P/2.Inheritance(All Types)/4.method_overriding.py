'''
METHOD OVERRIDING is:
When the child and the parent class have their separate but with the same name , then the object of the child class will by default use the method defined within the child class over the parent class. 
'''

class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot.")
        
rabbit = Rabbit()
rabbit.eat()