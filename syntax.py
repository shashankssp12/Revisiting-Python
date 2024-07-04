# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Mastery
# Author:      Shashank S Pandey
# Copyright:   (c) Shashank S Pandey 2024
# -------------------------------------------------------------------------------
print("Hello World")
name="Shashank"
middle_name=input("Enter your middle name")
is_cool=True
print("Python Master "+name+" "+middle_name+"Testing")
print(is_cool)

# TypeConversion --> used as python stores everything as strings
old=input("Enter age:")
new=old+2 # error:can only concatenate str (not "int") to str
print(new)

# Using type conversion
n=input("no.")
n1=int(n)+2
print(n1)
# Can Use:str(),bool(),float()<--Other type conversion functions

# Sum of two no.
n1=input("Enter first no.")
n2=input("Enter second no.")
n3=int(n1)+int(n2)
# print(n3)
print("sum:"+str(n3))


# CALCULATOR
a=int(input("Enter Num1:"))
b=int(input("Enter Num2:"))
op=input("Enter operation(+,-,%,/,*):")
if op=='+':
    print(a+b)
elif op=='-':
     print(a-b)
elif op=='*':
     print(a*b)
elif op=='%':
     print(a%b)
elif op=='/':
     print(a/b)
else :
     print("Invalid operation")

# RANGE keyword 
num=range(5)#it does not include 5(last digit) thus-->0,1,2,3,4
print(num)


#  INFINITE LOOP
i=1
while i!=0:
    print(i)
    i+=1 
    if i==7000:
        break

# NORMAL LOOP
i=0
while i<100:
    print(i)
    i+=2

#   PATTERN PROGRAMS-->With while loop
j=1
while j<=5:
    print(j * "*")
    j+=1
i=5
while i>0:
    print(i * "*") #multiplying the string i times
    i-=1

# FOR LOOP
for i in range(5):
    print(i)

# DATA 
data=[10,20,30,'hi']
i=0 
while i< len(data):
    print(data[i])
    i+=1
print("Out of loop")

# Reverse
i=len(data)-1
while i>=0:
    print(data[i])
    i-=1
print("out of loop")
data.clear()#clears my list
print(data)

# BREAK & CONTINUE
lis=[12,21,33,22]
i=0
while i<=len(lis):
    if lis[i]==33:
        continue
    print(lis[i])
    i+=1
print("out of loop")

# FOR LOOP IN LIST
data=["Java","C","Python","Ruby","Pearl"]
for i in data:
    if i=="Ruby":
        break # continue
    print(i)#prints names 1 by 1

# TUPLES()-->Like list but Immutable(cannot update, modify and delete values)
marks=(12,21,11,22,11)
# print(marks.append("shashank"))#cannot update, add
print(marks.count(11))#tells the frequency of a certain element--IN tuples
print(marks.index(11))#give the index of the element's first occurance


#  SETS{}-->no index-->UNORDERED
# No Indexing, starts from count one and can access via loops 
# As SETS have no repeated value so in console it show only unique values

marks={21,11,12,22,22,11}
# print(marks)#-->{11, 12, 21, 22}
for i in marks:
    print(i)#again repeated values won't come

# DICTIONARY{KEY:VALUE,KEY1:VALUE1}
speed={"d":60,"k":48,"h":33} 
print(speed["d"])
speed["k"]=23#it gets added in the dictionary
print(speed)
  
# FUNCTIONS:A block of code which is executed only when it is called 
#In-built functions,module functions,User-defined functions
def addno(first, second=1):#if nothing gets passed in second than automatically one will be used
    print(first + second)

addno(3,4) #Calling function
# 🌟The values a function is going to take as input are called Parameters
# 🌟The values we put in a called function are Arguement  

# STRING-->Indexing[] and slicing()
name="Bro Code"
# indexing
# [inclusive:exclusive:step]
print(name[:3] +" "+name[4:])
print(name[::2])
# Reversed name:
print(name[::-1])

# STRING USING SLICING

