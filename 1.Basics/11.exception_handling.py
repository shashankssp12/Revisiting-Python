'''
When we have some nutorious block of code that may throw an Error.
That maybe because of wrong input.
Solution:
try:-->handles the code by looking for the error in the except block
except:-->catches the code with specific error, or general and does what it is assigned(here we just print the error)
else:--> If no expection occurs then only this block will run.
finally:--> This will always execute , matters not if there's an error or not. (Use Case: To close an opened file)
'''
try:
    numerator=int(input("Enter Numerator"))
    demominator=int(input("Enter Denominator"))
    result = numerator/demominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print("You must enter a number")
except Exception as e: #it's a good practice to have this at the end, just in as an error comes that we haven't thought of.
    print(e)
else:
    print(result) 
finally:
    print("This will always execute")