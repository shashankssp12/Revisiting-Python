'''
multiple inheritance : When the child class is derived from more than one parent class
'''

class Predator:
    def hunt(self):
        print("This animal can hunt")

class Prey:
    def flee(self):
        print("This animal can flee")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# Fish Class has access to properties of both the Prey and Predator class (As fishes can be a Predator and Prey) 
class Fish(Prey, Predator):
    pass

r1 = Rabbit()
r1.flee()

h1 = Hawk()
h1.hunt()

f1 = Fish()
f1.flee()
f1.hunt()