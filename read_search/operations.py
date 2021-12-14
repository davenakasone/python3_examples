"""
cleans up the main()  places most of burden to this module
"""

import copy

#========================================================================================================================
#------------------------------------------------------------------------------------------------------------------------
def get_input():
    """ Get the data """
    transfer = ''
    with open("pi_million.txt") as file_object:
        temp = copy.deepcopy(file_object.read())
        transfer = copy.deepcopy(temp.strip())
    
    input_string =''
    for element in transfer:
        if element == '.' or element == '1' or element == '2' or element == '3' or element == '4' or element == '5'\
        or element == '6' or element == '7' or element == '8' or element == '9' or element == '0':
            input_string += element
        else:
            continue
            
    return input_string

#------------------------------------------------------------------------------------------------------------------------
def print_first_100(any_list):
    """ Lets you know what length is, prints first 100 elements... """
    length = len(any_list)
    print("elements in list: ", length)

    counter = 0
    stop = 100
    print("The first 100 chars of PI:  ", end = '')
    while counter < stop:
        print(any_list[counter],end='')
        counter += 1
    print('\nnotice the "3" and "." make two additional characters, so there are exactly 1 million decimals\n')

#------------------------------------------------------------------------------------------------------------------------
def birth_in_first_million(any_list):
    birthday = input("enter birday MMDDYY: ")
    if birthday in any_list:
        result = 'your birthday IS in the first 1 million decimals of pi'
    else:
        result = 'your birthday IS NOT in the first 1 million decimals of pi'

    return result

#------------------------------------------------------------------------------------------------------------------------
def zero_count(any_string):
    zeros = 0
    for element in any_string:
        if element == '0':
            zeros += 1
    return zeros

#------------------------------------------------------------------------------------------------------------------------
def A_count(any_string):
    As = 0
    for element in any_string:
        if element == 'A':
            As += 1
    return As

#------------------------------------------------------------------------------------------------------------------------
def scrub(any_string):
    """ Take of non BCD characters, keeps decimal """
    temp = ''
    for element in any_string:
        if element == '.' or element == '1' or element == '2' or element == '3' or element == '4' or element == '5'\
        or element == '6' or element == '7' or element == '8' or element == '9' or element == '0':
            temp += element
        else:
            continue
    return temp
    
#========================================================================================================================
#                                           ~ ~ ~ END ~ ~ ~                                                             #
#========================================================================================================================
