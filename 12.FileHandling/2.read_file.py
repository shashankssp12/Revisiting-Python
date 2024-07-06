'''
with open() --when used, automatically closes any file that is being opened.
Also its a good practice to handle FileNotFoundError
'''
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("Couldn't find the file :/")
    