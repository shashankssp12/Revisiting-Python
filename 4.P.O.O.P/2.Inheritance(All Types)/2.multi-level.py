'''
Multi-level Inheritance: child class has access to all the properties of its, parent class and also to the properties of parent's parent-class.
'''

# Organism --> Humans --> Student

class Organism:
    lifeSpan=None
    alive = True

class Human(Organism):
    origin="Indian"
    def eats(self):
        print("Humans eat")
    def thinks(self):
        print("Humans think")

class Student(Human):
    rollNo = None
    def studies(self):
        print("This student studies")
        
# ##################
'''
Now here Student class has access to all properties of Human and Organism class.
'''

s1 = Student()
print("This Student is alive?",s1.alive)
print(s1.origin)
s1.eats()
s1.thinks()
s1.studies()