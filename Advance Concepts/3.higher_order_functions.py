'''
Higher Order Functions: These are functions that either:

                        1.Take Functions as arguments.
                        OR'
                        2.Return Functions 
'''
#  ## Example 1
def func1(str):
    print(str)
    
def higherOrderFunc(func):
    textShow = func("HELLO")
    
higherOrderFunc(func1)

#  ## Example 2:
def greet(str):
    print(str + "World!")
def say_something(func):
    func("Hello")

say_something(greet) # HelloWorld!

# -----------------------------------------------------------------------------
# HOF: that return function

# Ex: 10/2 =5   #here 2 is divisor 10 is dividend
def divisor(x):
    def dividend(y):
        print(y/x)
    return dividend
# The divisor function will need a number to be input later.

Enter_dividend = divisor(5)
Enter_dividend(5) # the result must be 1