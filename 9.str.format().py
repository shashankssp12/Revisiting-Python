'''
.format()--> gives more control over the presentation of the string.

'''
# text="The big brown fox jumps over the lazy dog"
# #What if we want to have animals of our choice.

animal1="dog"
animal2="fox"
## Way 1--> By using positional arguments
# print("The {} jumps over the {}".format(animal1,animal2))

# # Better way
# text="The {} jumps over the {}"
# print(text.format(animal1,animal2))

# # Can give numbering as well in the string 
# text="The {0} jumps over the {0}"
# print(text.format(animal1,animal2))

# print(text.format(animal1,animal2))

## Way2 --> By using keyword arguments in a better way

# text="The {a} jumps over the {b}"
# print(text.format(a="Elephant",b="Rhino"))

# ---------------------------# #Flexibile Formatting
'''
{:}
{:5}
{:>5}
'''
a="Elephant"
# text="The {:55} jumps!"
print("The {:20}jumps!".format(a)) #20 spaces after Elephant
print("The {:<20}jumps!".format(a)) # same result
print("The {:>20}jumps!".format(a))
print("The {:^20}jumps!".format(a)) # placed in center

# -----------With Numbers-------------

number=3.14159
print("The number pi is {:.2f}".format(number))
number2=14234
print("Number is {:,}".format(number2))
print("Number is {:b}".format(number2)) #gives binary of the number

'''
 method in Python returns a new string with the formatted values. It does not modify the original string but instead creates and returns a new one.
 '''