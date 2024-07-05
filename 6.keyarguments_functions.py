''' 
To Note: 
Order of arguments(if many) must be paid attention to, as it may result in inconsistent results.
'''
# EXAMPLE ONE
# def func1(first,last):
#     print(first+" "+last)
    
# def input():
#     str1="shashank"
#     str2="pandey"
#     func1(str2,str1)# output--> pandey shashank

#EXAMPLE 2
# def division(a,b):
#     print(a/b)
# a=5 
# b=0
# division(a,b)   #error


######### To avoid such situations #############
# Use keyword arguments

# EXAMPLE ONE
def func1(first,last):
    print(first+" "+last)
    
str1="shashank"
str2="pandey"
func1(last=str2,first=str1)# output--> shashank pandey

# These are called keyword arguments, literally meaning that we define the parameter for what we are sending the data🌟