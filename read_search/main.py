"""
not really going to put in 1 million digits, but it is possible. This one only has a few hundered
you could run as much data through as your memory can handle
"""

import copy
import operations as ops
#========================================================================================================================
#------------------------------------------------------------------------------------------------------------------------

pi_string = copy.deepcopy(ops.get_input()) # string to hold first 1M decimals of pi   and the "3."    cleans white space
ops.print_first_100(pi_string)  # just to check

birth = ops.birth_in_first_million(pi_string) # is your birthday in PI?
print(birth)

# replace 0's with A's
print("\ncurrently, there are [ ",ops.zero_count(pi_string)," ] zeros   and [ ",ops.A_count(pi_string)," ] A's")
pi_string = copy.deepcopy(pi_string.replace('0','A')) # stay deep
print("currently, there are [ ",ops.zero_count(pi_string)," ] zeros   and [ ",ops.A_count(pi_string)," ] A's")
pi_string = copy.deepcopy(ops.scrub(pi_string))
print("currently, there are [ ",ops.zero_count(pi_string)," ] zeros   and [ ",ops.A_count(pi_string)," ] A's")

#========================================================================================================================
#                                           ~ ~ ~ END ~ ~ ~                                                             #
#========================================================================================================================
