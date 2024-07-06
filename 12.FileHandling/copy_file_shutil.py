'''
Using the Shutil module:
copyfile() --> copies the content of the file
copy() --> copyfile() + permission mode + destination can be a dir
copy2() --> copy() + copies meta-data (file's creation and modification details)
'''
import shutil
path = 'D:\\Revisiting Python\\test.txt'
shutil.copy(path,'D:\\Revisiting Python\\copy.txt') # source, destination