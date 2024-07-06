'''
"os" module is already in python standard lib so we just need to import it.
'''
import os
path1 = "D:\\Revisiting Python\\12.FileHandling"
# path="C:\\Users\\shash\\Desktop\\test.txt" # use \\ instead of \ in string as this is an escape sequence for the string to understand that this is not just a charater in a string

if os.path.exists(path1):
    print("The location exists")
    if os.path.isdir(path1):
        print("It's a directory")
    elif os.path.isfile(path1):
        print("It's a file")
else:
    print("Location doesn't exist")