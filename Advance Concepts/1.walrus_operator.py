# Walrus Operator :=
# Its feature for Python 3.8 and beyond
#  Assigns values to variables as part of larger expression.

# use cases
print(happy:=True) #can be able to print the values at the time of assigning

# Trick Question: ---Guess the output
# while(happy := True):
#     print(happy)
#     happy = False
    
    
# ######## Usual Way of writing:

# foods = [] # or foods = list()
# while True:
#     food = input("What food do you like?")
#     if food != "quit":
#         foods.append(food)
#     else:
#         break

# print(foods)

################# The Walrus Way of writing:

Food_list = list()
while food := input("Enter") != "quit":
    Food_list.append(food)

print(Food_list)

# not so good examples as , it makes the foodlist to store only True values until false