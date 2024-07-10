# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Mastery
# Author:      Shashank S Pandey
# Copyright:   (c) Shashank S Pandey 2024
# -------------------------------------------------------------------------------


# # FOR LOOP
# for i in range(5):
#     print(i)

# # DATA 
data=[10,20,30,'hi'] #---> List[]
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
'''
By default for loop doesn't have access for indexes to items in the list.
can use enumrate
'''
for idx, item in enumerate(data):
    print(idx,item)


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




# # Reverse
# i=len(data)-1
# while i>=0:
#     print(data[i])
#     i-=1
# print("out of loop")
# print(data)
# data.clear()#clears my list , thus empty list
# print(type(data))





