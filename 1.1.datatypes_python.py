'''
int -->10 -10
float--> 10.45
complex --> 10+10i
strings--> "Hello" or 'Hello'
lists--> [1,'hello', 4.5, "A"] #mutable list[1]-->hello
tuples--> (1,'hello', 4.5, "A") #immutable tuple[1]-->hello
dictionary -->{'a':22, 'b':44.4} # usage dict['a']-->22
boolean (bool class) isSorted = True 
set --> {1,'Hello','Hello',1,"A"} ---> on printing no repeated values are shown, a set is non indexed.
'''


# Strings:
# my_variable = "This is \
# too big to fit \
# on a single line"
# print(my_variable)

##multi-line string
# my_variable = """This is 
# too big to fit 
# on a single line"""
# print(my_variable)


name = "Shashank"
print(name[3])
print(len(name))
new_name = name + " Shekhar"
print(new_name)





# # TUPLES()-->Like list[] but Immutable(cannot update, modify and delete values)
# marks=(12,21,11,22,11)
# # print(marks.append("shashank"))#cannot update, add
# print(marks.count(11))#tells the frequency of a certain element--IN tuples
# print(marks.index(11))#give the index of the element's first occurence


# #  SETS{}-->no index-->UNORDERED
# # No Indexing, starts from count one and can access via loops 
# # As SETS have no repeated value so in console it show only unique values

# marks={21,11,12,22,22,11}
# print(marks)#-->{11, 12, 21, 22} in ascending order
# for i in marks:
#     print(i)#again repeated values won't come

# # DICTIONARY{KEY:VALUE,KEY1:VALUE1}---> Key-Value Pair
# speed={"d":60,"k":48,"h":33} 
# print(speed["d"])
# speed["k"]=23#it gets added in the dictionary
# print(speed)