"""
The simplest way to handle exceptions is with a "try-except" block:
"""
(x,y) = (5,0)
try:
    z = x/y
except ZeroDivisionError:
    print ("divide by zero")


"""
to examine:
"""
(x,y) = (5,0)
try:
    z = x/y
except ZeroDivisionError as e:
    z = e # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
    print (z) # output: "integer division or modulo by zero"

"""
you should only catch what you can handle, but if you want to catch all:
MoinMoin macro, raise, finally
"""
import sys
try:
    x = 2 / 0   #untrusted.execute()
except: # catch *all* exceptions
    e = sys.exc_info()[0]
    print(e)   #write_to_page( "<p>Error: %s</p>" % e )