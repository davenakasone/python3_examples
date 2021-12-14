
import random       # using random.randint(min, max)
import json
import copy         # using copy.deepcopy(var)
import os           # using os.system('clear')
import time         # using sleep()
import datetime     # for current time use    current_time = datetime.datetime.now()
#========================================================================================================================
#------------------------------------------------------------------------------------------------------------------------
def fill_list(any_list):
    """ bring in a list, clear it, fill it with random number """
    any_list.clear() 
    size = random.randint(5,15)
    counter = 0

    while counter < size:
        element = random.randint(50,99)
        any_list.append(element)
        counter += 1
    
    return any_list

#------------------------------------------------------------------------------------------------------------------------
def test_print_list(current_list):
    "just call to get a test pring of a list, string, or most itterables"
    length = len(current_list)
    counter = 0
    print ("current list:  [ ",end = '')
    while counter < length:
        if counter != length - 1:
            print(current_list[counter], " , ", end = '')
        else:
            print(current_list[counter], "]")
        counter += 1

#------------------------------------------------------------------------------------------------------------------------
def pass_json(fname):
    with open(fname) as f:
        variable = json.load(f)
    return variable







#========================================================================================================================
#                                           ~ ~ ~ END ~ ~ ~                                                             #
#========================================================================================================================