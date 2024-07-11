'''
method chaining: it is calling of methods sequentially of the same object, each funciton returns self
'''
# When we create a method in python and retun nothing, python will by-default return None. 

class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You used the brakes")
        return self

    def turn_off(self):
        print("You stop the car")
        return self
# How we usually do it

car = Car()
car.turn_on()
car.drive()
car.brake()
car.turn_off()

print("*************************************")
# Cooler way of doing it. 

car.turn_on().drive().brake().turn_off()
# This gives error, because we must use ---> return self

# 1. `return self` in methods allows chaining: `object.method1().method2()...`.
# 2. Keeps the same object for all chained methods.
# 3. Maintains object state across modifications.

print("*************************************")
# Better formatting
car.turn_on()\
        .drive()\
            .brake()\
                .turn_off()
