"""
don't always have to start fresh (DRY) 
parent has originals, child takes all of that  
you'll probably want to call the __init__() to take the original attributes and make them available in the child

if the parent class is in the same file, you need to have it appear before the child (or just use files to seperate)
for the "over-ride" just name method of parent with same name in child....parent's method is disregarded
not too much safety for attributes (variables) that would normally be private in c++    no control of class resources/members

I'll stick with full import because it forces .  and avoids naming conflicts
"""

import electric_cars  # only need the child here     ... or from electric_cars import ElectricCar
                      #     ... or        from module_name import *         to get all the classes, like functions in a module 
                      #      module_name.ClassName     is the prefered way  no abiguity
                      # for long programs, alias also ok       from electric_cars import ElectricCars as EC 
#========================================================================================================================
#------------------------------------------------------------------------------------------------------------------------

my_ev = electric_cars.ElectricCar('Nissan', 'Leaf', 2020)
print(my_ev.get_description())
my_ev.print_battery()

# print(my_ev.gas_tank) # before overide/delete attribute, this was directly inhereted  delete or overide as needed
my_ev.gas_tank_specs()  # ideally you'd want to private this away, but python makes it hard

# use the composed class also ('Charging')...reference the attribute that holds the composed class, then method/attribute
print("the closest charging station is in",my_ev.charging_info.closest())
my_ev.charging_info.print_battery_specs()
print("this vix will take",my_ev.charging_info.charge_time,"hours to charge")
my_ev.print_mpg()    # redefined/overwritten from base using a composition attribute

print("\n")
#nest, adjust within class (can call parent, or adjust composed attributes)
my_ev.battery_upgrade(100) # update it
my_ev.print_mpg()   
#========================================================================================================================
#                                           ~ ~ ~ END ~ ~ ~                                                             #
#========================================================================================================================