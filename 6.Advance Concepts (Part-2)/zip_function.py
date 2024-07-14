'''
zip(*iterables): it combines the elements within multiple-iterables and then returns a zip object.
                 It gives an iterator of tuples. Simply the data is grouped in tuple format.
'''

# List 1
list1 = [1, 2, 3, 4, 5]

# List 2
list2 = ['a', 'b', 'c', 'd', 'e']

# List 3
list3 = [True, False, None, 'Hello', 10.5]

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)


# ------------------------Example-1

zipped = zip(list1,list2,list3)
print(type(zipped))
for item in zipped: 
    print(item)
    
# If the length of iterables vary then the zipped iterable will have the aggregated iterables of shortest iterable. super tough language, but I get it.!