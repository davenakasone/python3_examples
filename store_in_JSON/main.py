"""
you'll get a lot of program that rely on storing data
the json module lets you keep user data after program closes...decent state initializer and holder
you dump simple python data structures into a file and load the data from that file next time program runs

it can also share data between different programs
JSON is java script object notation and not specific to python, it is written in C and C++ by real programmers

Python	     JSON
dict	     Object
list	     Array
tuple	     Array
str	         String
int	         Number
float	     Number
True       	 true
False	     false
None	     null

simple way to share data between programs
"""
import random       # using random.randint(min, max)
import copy         # using copy.deepcopy(var)
import os           # using os.system('clear')
import time         # using sleep()
import datetime     # for current time use    current_time = datetime.datetime.now()
import json

import operations as ops
import another_main as another
#========================================================================================================================
#------------------------------------------------------------------------------------------------------------------------
filename = 'vars.json'
var1 = []
var1 = ops.fill_list(var1)
ops.test_print_list(var1)
print(f"will store list in [ {filename} ]   ...open file to see")

with open(filename, 'w') as f:
    json.dump(var1, f)
    f.write('\n')

# the program can close, share, or anything else. another variable will take [var1] from vars.json
filename = 'vars.json'
var2 = ops.pass_json(filename)
print("\n[var2] has successfully recieved [var1] through the JSON file")
ops.test_print_list(var2)

another.another_program()

print ( "\n     ~ ~ ~ PROGRAM COMPLETE ~ ~ ~     " )
#========================================================================================================================
#                                           ~ ~ ~ END ~ ~ ~                                                             #
#========================================================================================================================