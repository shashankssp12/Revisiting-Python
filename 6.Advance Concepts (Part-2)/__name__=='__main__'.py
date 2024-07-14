'''
__name__ is used to check if the module in use is being directly accessed or it getting accessed indirectly.
'''



import zip_function
# though the zip_function module is just begin imported , then also it runs because nothing is in function.

if __name__ == '__main__':
    print("This runs only when the module is run directly and I can be used to run tests then")
else:
    print("This module is imported")
    print("This is when the module is being accessed as an import / indirectly")

# sadly this file/module cannot be imported easily as this has a bad naming.



'''
 The `__name__` variable in Python is a special built-in variable that is automatically set in a Python script. When a Python script is executed, Python assigns the `__name__` variable different values depending on how the script is being used.

In short, the `__name__` variable is mainly used to control the behavior of a Python script when it is being imported as a module or run as the main program.

A common use case for the `__name__` variable is to include a block of code that should only run when the script is executed directly (as the main program) and not when it is imported as a module into another script. This is often achieved by checking the value of `__name__`:

```python
if __name__ == "__main__":
    # Block of code that should only run when this script is executed directly
    # Main program logic goes here
```

By using `if __name__ == "__main__":`, you can ensure that certain code blocks, like test code or initialization code, are only executed when the script is run directly, not when it is imported as a module into another script. This helps in keeping your code modular and reusable.
'''