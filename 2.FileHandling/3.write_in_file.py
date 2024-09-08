'''
open(path,'w')# this over writes the current file
open(path,'a') #this appends the content in the current file
'''

import os

path = "D:\\Revisiting Python\\test.txt"
text="It is what it is\nThis is some text"
if(os.path.exists(path)):
    with open(path,'a') as file:
        file.write(text)


'''
we can at the same time create new files
'''

with open('new.txt','w') as file:
    file.write("This is a newly created file") # file gets created in the main/parent folder
    
    file.writelines("I can write \n multiple lines now ")