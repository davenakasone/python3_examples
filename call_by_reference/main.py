"""
set up temporary variables
use [:] for a copy
just remember everything is dynamic
like c++, you want to pass by reference if possible ( a lot more efficient )
"""
import random
#========================================================================================================================
#------------------------------------------------------------------------------------------------------------------------

def delete_all(anyList):
    #del anyList[:]
    anyList.clear()

#------------------------------------------------------------------------------------------------------------------------

def print_list(anyList):
    if len(anyList) != 0:
        counter = 0
        length = len(anyList)
        print("{ ", end ='')
        while counter < length:
            if counter != length - 1:
                print(myList[counter], end = " , ")
            else:
                print(myList[counter], end = " }")
            counter += 1
        print("  ... the list now")
    else:
        print("the list is empty, looks like the function call mutated the list")

#------------------------------------------------------------------------------------------------------------------------
def initialize():
    freshList = []
    length = random.randint(10,20)
    counter = 0
    while counter < length:
        freshList.append(random.randint(50,90))
        counter += 1
    return freshList

#------------------------------------------------------------------------------------------------------------------------

myList = initialize()
print_list(myList)
delete_all(myList)
print_list(myList) # because you passed it by reference...everything is dynamic
print("\n")
myList = initialize()
print_list(myList)
delete_all(myList[:]) # now it is passed by value/copy, so function can change it all it wants, won't enter this scope
print_list(myList)
print("passing a copy didn't allow changes to effect this scope, list remains unchanged")




