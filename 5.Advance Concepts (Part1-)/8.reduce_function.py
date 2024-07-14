'''
reduce(): This function works on the first two elements of the iterable and works upon them and turns it into a single value . The Process Repeats until only one element in left.

reduce(function,iterable)
must import functools

'''
from functools import reduce

# The  usual way of adding all elements in a list: 
# list = ['H','E','L','L','O']
# word=""
# for i in list:
#     word = word+i
# print(word)

# The advance way - reduce way of doing it.
list1=['H','E','L','L','O']

print(word := reduce(lambda x,y:x+y,list1))

# # EXMAPLE 2:

factorial = (5,4,3,2,1)
print(value := reduce(lambda x,y : x*y ,factorial))