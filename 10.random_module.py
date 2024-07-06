'''
random is a module , it has many functions in it.
'''
import random

dice=random.randint(1,6)#both numbers are inclusive
print(dice)

x= random.random()# generates a number b/w 0 n 1
print(x)

my_list=[1,2,3,4,5,6,7,8,9,'J','Q','K','A']
choice = random.choice(my_list)
random.shuffle(my_list)#it shuffles the existing list
print(choice)
print(my_list)