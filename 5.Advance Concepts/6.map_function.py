'''
*an iterable is a list, tuple etc...
map(function, iterable): It applies a function to each item within an iterable

Returns a map object-->easily typecasted
'''

list_items = [
        ("item1",4.00),
        ("item2",2.00),
        ("item3",5.00),
        ("item4",64.00),
        ("item5",23.00)
       ]

add_some = lambda col:(col[0],col[1]*10) # after : what_the_expression returns
new_list = list(map(add_some,list_items))
print(new_list)