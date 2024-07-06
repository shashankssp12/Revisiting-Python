'''
The os.replace function tries to move the file, which isn't possible across different drives.

To handle this, you should copy the file instead of moving it. You can use the shutil
'''

import os
source="text.txt"# no need to define the full path if the file/dir exists in the same dir of this file
destination="C:\\Users\\user\\Desktop\\text_new.txt"

try:
    if os.path.exists(destination):
        print("File already present")
    else:
        os.replace(source,destination)
        
except FileNotFoundError :
    print(source+"File not found")
