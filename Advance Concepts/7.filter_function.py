'''
filter(function,iterable)--> Creates a collection of elements from an iterable for which the funciton returns True.

returns a filter object--->can be casted in list or so..
'''

list_items = [
        ("name1",15),
        ("name2",19),
        ("name3",21),
        ("name4",17),
        ("name5",18)
       ]
age_check = lambda data:data[1] >= 18

print(list(filter(age_check,list_items)))





