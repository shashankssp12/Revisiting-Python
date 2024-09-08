'''
with open() --when used, automatically closes any file that is being opened.
Also its a good practice to handle FileNotFoundError
'''
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print("Couldn't find the file :/")
    
    
# Now :
file = open('D:\\Revisiting Python\\2.FileHandling\\test.txt', mode='r')
data = file.readline()
data_all = file.readlines()# to read multiple lines
print(data)
file.close()

'''
The with open function is better for exception handling
'''