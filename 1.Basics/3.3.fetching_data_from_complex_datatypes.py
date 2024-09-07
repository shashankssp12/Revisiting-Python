# list=[1,2,'hi',3.5]
# for i in list:
#     print(i)

# dict={3:'Shashank',2:'Madhu'}

# order = {3,2}

# for i in order: 
#     print(dict[i])

# for i in dict.items():
#    print(i)
# for i in dict.values():
#     print(i)


# Now for more complex dictionary:

dict={
    1:{'name':'shashank'},
    2:{'name':'madhu'}
}

list = [1,2]
for i in list:
    print(dict[i]['name'])

