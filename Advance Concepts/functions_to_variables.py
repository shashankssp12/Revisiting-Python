'''
Long story Short:
You can assign the name of the funcion(without parenthesis)to a variable and then use that variable as the function

this is actually super cool
'''

def hello():
    print("You'll make it!")

hi = hello
print(hello)
print(hi) #prints the memory location of hello function

hi() # runs the hello method

show = print
show("Whao! I can't believe that works!!") # it actually works