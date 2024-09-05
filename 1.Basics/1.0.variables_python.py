'''
Maintain proper naming convention.
Use :
-Camel Case: myName
-Snake Case: my_name

But follow it consistently through out.
'''

#Must know:
a,b,c = 1,2,3

x=y=z=10 

'''
Why python is called a Dynamically Typed Language? 

"Dynamically typed" means that the type of a variable is determined at runtime rather than at compile-time. You do not need to declare the type of a variable when you create it; the interpreter infers the type based on the value assigned.
'''


'''
Scope of variables in Python:
-Global example: variable declared outside of function
-Local example: function
-Enclosed   example: nested function
-Built-in example: print, len, range, etc.
'''

GLOBAL_VAR = 10

def fn1():
    local_var = 20
    # print(enclosed_var) #Error: enclosed_var is not defined
    def fn2():
        enclosed_var = 30
        print(GLOBAL_VAR)
        print(local_var)
        print(enclosed_var)
        # All can be accessed here
    fn2()
    # print(enclosed_var) #Error: enclosed_var is not defined    