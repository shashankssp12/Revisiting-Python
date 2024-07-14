'''
List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range) and optionally filtering items with a condition. The syntax is:

[expression for item in iterable if condition]


list comprehension : Is a way of writing lists with less syntax. 
                     Certain lambda functions can be mimiced, easier to read.
                     3 ways:
                     [var_name for var_name in iterable]
                     [var_name for var_name in iterable if condition]
                     [var_name if condition else statment for var_name in iterable] 
                    
'''

marks = [100,88, 39, 89, 23,67, 75,53]
list0 = list(filter(lambda x:x>=60,marks))
print(list0)
list1 = [i for i in range(0,11) ]
list2 = [i for i in marks if i>=60]
list3 = [i if i>=2 else "something" for i in range(0,11)]

print(list1, list2, list3, sep="\n") 