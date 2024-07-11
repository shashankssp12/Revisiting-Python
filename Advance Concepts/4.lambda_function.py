'''
Lambda function--> It is a function written in one line,
                   It accepts any number of parameters, but has only one expression.
                   (It's like a shortcut)
                   (useful, if needed for short period of time)
'''
# Example-1
add = lambda x,y : x+y
print(add(4,5))


# Example-2
multiply = lambda x,y : x*y
print(multiply(4,5))

# Example-3
enter_name = lambda first_name, last_name : "Hi! "+first_name +" "+ last_name
print(enter_name("Shashank","Shekhar"))

# # Example-4
check_age = lambda age : True if age>=18 else False
print(check_age(34))