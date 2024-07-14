# *args --> when you have to send many variable or unset number of items to be sent as argument ,you use --> * 
# 🌟🌟 IT SEND DATA IN TUPLE ____________AND YOU CAN'T MODIFY TUPLE UNTIL YOU CAST IT🌟🌟
# Ex:

# def sum(a,b):
#     return a+b;
# print(sum(2,4,5)) #TypeError: sum() takes 2 positional arguments but 3 were given

# To tackle this, instead do:

def sumPro(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
 
print(sumPro(3,5,35,3,6))# 52

# Cool stuff