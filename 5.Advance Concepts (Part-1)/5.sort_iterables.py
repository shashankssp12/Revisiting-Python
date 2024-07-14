'''
sort():
- it is a built-in method for lists 
- thus usage list_name.sort()

Other than this , sort can used as a function like "sort(pass)" for other iterables other than list.
sorted(pass_tuple,reverse = True)

Returns ---> LIST
'''
# LEVEL 1:

list = ['a','z','b','d','c','w','d']
list.sort(reverse=True)
# print(list) # sorts the list alphabetically

tuple = ('a','z','b','d','c','w','d')
# tuple.sort() # error
# 
# sorted_tuple = sorted(tuple)
# print(sorted_tuple)

# Level-2 More complex data

student_details= [ #LIST of TUPLES
                    ("B",4,"Y"),
                    ("C",3,"X"),
                    ("D",2,"W"),
                    ("A",5,"Z"),
                    ("E",1,"V"),
                 ]
# # student_details.sort()
# #arranges the list in alphabetically order, with column 1(A,B,C,..)
# for i in student_details:
#     print(i) 

# What if we want to sort according to 2nd column(index 1) of the tuples (the numbers)
'''
That's where the "key" keyword comes to play in the sort function.
'''
# variable as a fuction
col = lambda cols:cols[1]
student_details.sort(key=col)
print(student_details) #Arranged by numbers
