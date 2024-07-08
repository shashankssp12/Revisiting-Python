'''
module--> It is a file containing some python code.There can be Classes, functions,etc.
#Used in modular programming, which is to seperate a program into parts
'''
# This file can be a module as well:
# But let's make a module to import here--->myModule.py
'''
import myModule as mm # alias can be made for modules with longer names and more usage

#Usage
mm.hello()
mm.bye()
'''
# There something cool I found, how to import module with not to conventional names , like--->12.1.myModule.py 🌟‼️ 
# We use : importlib module.


# Here'ss what to do:
import importlib.util
import sys
from pathlib import Path

# Define the module name and path
module_name = '12.1.myModule'
module_path = str(Path('12.1.myModule.py').resolve())

# Load the module
spec = importlib.util.spec_from_file_location(module_name, module_path)
my_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = my_module
spec.loader.exec_module(my_module)

# Now you can use my_module just like any other imported module
my_module.bye()

