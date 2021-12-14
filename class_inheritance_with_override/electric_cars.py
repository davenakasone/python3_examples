
"""
2 things hanpening:
- noticed electric cars share most attributes as regular cars -> inheret
- noticed a lot of unqiue info needed (battery) -> new class

taking a 'Charging' instance to this class is like the C++ compisition

can store each class in its own module, but most people store related classes inside a single module
"""

import cars              # or use:    from cars import Car
import charging          # from charging import Charging           multiple classes seperated by , if from same module
#========================================================================================================================
#                                           < class >  ElectricCar                                                      #
#========================================================================================================================
class ElectricCar(cars.Car):   #need to reference parent to inheret
    
    #--------------------------------------------------------------------------------------------------------------------
    def __init__(self, make, model, year):
        super().__init__(make, model, year)    # special function to call parent  ... now that child is good, add what you want
        self.battery_size = 75                 # none of this gets associated with the parent, add all attributes you want
        self.charging_info = charging.Charging() # now you brought entire class into 1 attribute

        #self.gas_tank = 30                     # override default of attribute
        del self.gas_tank                      # remove attribute
        #del super().gas_tank_specs             # as for deleting methods....have to get creative
        # this is pretty ugly...mutilate parent, make a blank function, not too many options
        
    #--------------------------------------------------------------------------------------------------------------------
    def print_battery(self):
        print("this is a",self.battery_size,"kWh battery")
    
    #--------------------------------------------------------------------------------------------------------------------
    def gas_tank_specs(self):
        print("mf, ev's don't have gas tanks")

    #--------------------------------------------------------------------------------------------------------------------
    def print_mpg(self):
        range = self.charging_info.volts / 10
        print("this EV will go around: ", range,"miles")

    #--------------------------------------------------------------------------------------------------------------------
    def battery_upgrade(self, new_size):  # can't call back and forth between composed class, but can change things
        self.battery_size = new_size
        self.charging_info.volts = new_size * 100
#========================================================================================================================
#                                           < / class >  ElectricCar                                                    #
#========================================================================================================================