# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Mastery
# Author:      Shashank S Pandey
# Copyright:   (c) Shashank S Pandey 2024
# -------------------------------------------------------------------------------
# print("Hello World")
# name="Shashank"
# middle_name=input("Enter your middle name")
# is_cool=True
# print("Python Master " +name+" "+middle_name)
# print(is_cool)

# # TypeConversion is used as, python stores everything as strings
# old=input("Enter age:")
# new=old+2 # error:can only concatenate str (not "int") to str
# print(new)

# # Using type conversion
# n=input("no.")
# n1=int(n)+2
# print(n1)
# # Can Use:str(),bool(),float()<--Other type conversion functions

# # Sum of two no.
# n1=input("Enter first no.")
# n2=input("Enter second no.")
# n3=int(n1)+int(n2)
# # print(n3)
# print("sum:"+str(n3))



# RANGE keyword 
# num=range(1,5)#it does not include 5(last digit) thus-->0,1,2,3,4
# print(type(num))
# for i in num :
#     print("Python")

#  INFINITE LOOP
# i=1
# while i!=0:
#     print(i) 
# #     if i==7000:
# #         break

# # NORMAL LOOP
# i=0
# while i<100:
#     print(i)
#     i+=2

# #   PATTERN PROGRAMS-->With while loop
# j=1
# while j<=5:
#     print(j * "*")
#     j+=1
# i=5
# while i>0:
#     print(i * "*") #multiplying the string i times
#     i-=1

# # FOR LOOP
# for i in range(5):
#     print(i)

# # DATA 
# data=[10,20,30,'hi'] #---> List[]
# i=0 
# while i< len(data):
#     print(data[i])
#     i+=1
# print("Out of loop")

# for i in data:
#     print(i)
# Output is same for both:
# 10
# 20
# 30
# hi



# # Reverse
# i=len(data)-1
# while i>=0:
#     print(data[i])
#     i-=1
# print("out of loop")
# print(data)
# data.clear()#clears my list
# print(type(data))


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



