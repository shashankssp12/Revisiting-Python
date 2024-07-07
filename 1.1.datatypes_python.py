
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