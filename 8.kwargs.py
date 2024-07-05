'''
**kwargs --> **keyword argument is same as *args , it also allows multiple arguments but it puts them into DICTIONARY format as you define the keywords associated with the value.

'''
def printName(**kwargs):
    print(kwargs)
    # for key,value in kwargs:
    #     print(key+":"+value)

printName(a=4, b=5)

####################### To be continued#########################