import copy
#========================================================================================================================
#------------------------------------------------------------------------------------------------------------------------
def get_input():
    """ open the file, get the input, clean it up, and pass it to main program """
    message = []
    scrubbed = ''
    with open('input.txt') as file_object:
        for line in file_object:
            scrubbed = copy.deepcopy(scrub(line))
            message.append(copy.deepcopy(scrubbed))
    return message  

#------------------------------------------------------------------------------------------------------------------------
def scrub(any_string):
    """ Take off the white space and focus on the needed user input """
    scrubbed = ''
    counter = 0
    length = len(any_string)
    start = False
    
    while counter < length:
        element = any_string[counter]
        if element == ':':
            start = True
        if start == True and element != '\n' and element != ':':
            scrubbed += element
        counter += 1
    scrubbed = scrubbed.strip()
    return scrubbed

#------------------------------------------------------------------------------------------------------------------------
def test_print(any_obj):
    for item in any_obj:
        print(item)

#------------------------------------------------------------------------------------------------------------------------
def record(any_list):
    with open('output.txt', 'w') as file_object:
        counter = 0
        length = len(any_list)
        while counter < length:
            element = any_list[counter]
            if counter == 0:
                output = f"Name < {element} >\n"
                file_object.write(output)
            elif counter == 1:
                output = f"Message < {element} >\n"
                file_object.write(output)
            else:
                output = f"complaint_{counter} < {element} >\n"
                file_object.write(output)
            counter += 1
        
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#========================================================================================================================
#                                           ~ ~ ~ END ~ ~ ~                                                             #
#========================================================================================================================

"""

"""