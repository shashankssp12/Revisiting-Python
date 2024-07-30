'''
1.int -->10 -10
2.float--> 10.45
3.complex --> 10+10i
4.strings--> "Hello" or 'Hello'
5.lists--> [1,'hello', 4.5, "A"] #mutable list[1]-->hello
6.tuples--> (1,'hello', 4.5, "A") #immutable tuple[1]-->hello
7.range--> (0,5) #5 is exlusive
8.dictionary -->{'a':22, 'b':44.4} # usage dict['a']-->22
9.boolean (bool class) isSorted = True 
10.set --> {1,'Hello','Hello',1,"A"} ---> on printing no repeated values are shown, a set is non indexed.
11.frozenset (immutable set)
'''


# Strings:
# # Prints in a single line though
# my_variable = "This is \
# too big to fit \
# on a single line"
# print(my_variable)

##multi-line string
# my_variable = """This is 
# too big to fit 
# on a single line"""
# print(my_variable)


# name = "Shashank"
# print(name[3]) # s
# print(len(name)) # 8
# new_name = name + " Shekhar"
# print(new_name)



# # TUPLES()-->Like list[] but Immutable(cannot update, modify and delete values)
# marks=(12,21,11,22,11)
# # print(marks.append("shashank"))#cannot update, add
# print(marks.count(11))#tells the frequency of a certain element--IN tuples
# print(marks.index(11))#give the index of the element's first occurence


# #  SETS{}-->no index-->UNORDERED
# # No Indexing, starts from count one and can access via loops 
# # As SETS have no repeated value so in console it show only unique values

# marks = {21,11,12,22,22,11}
# # print(marks)#-->{11, 12, 21, 22} in ascending order
# for i in marks:
#     print(i)#again, repeated values won't come

# # # DICTIONARY{KEY:VALUE,KEY1:VALUE1}---> Key-Value Pair
# speed={"d":60,"k":48,"h":33} 
# print(speed["d"])
# speed["k"]=23#it gets updated in the dictionary
# # print(speed)

# Use:
questions = {
    "What is the largest mammal in the world?": "A",
    "How many continents are there on Earth?": "A",
    "What planet is known as the Red Planet?": "A",
    "What is the tallest mountain in the world?": "A"
    }
# for key in questions:
#     print(questions[key])
#     print(questions.get(key),end=" ")

 # There are several ways to iterate through a dictionary in Python. Here are the main methods:

# Iterate through keys:

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key)
    
# Iterate through values:
my_dict = {'a': 1, 'b': 2, 'c': 3}

for value in my_dict.values():
    print(value)
    
    
# Iterate through key-value pairs:
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(key, value)
    
    
# Iterate through keys using keys() method:
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict.keys():
    print(key)
    
    
# Iterate through keys and access corresponding values:
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key, my_dict[key])