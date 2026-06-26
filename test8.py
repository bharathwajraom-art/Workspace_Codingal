class Vehicle:
    def __init__(self,name,max_speed,milleage):
        self.name=name
        self.max_speed=max_speed
        self.milleage=milleage
class Bus(Vehicle):
    pass
school_bus=Bus("School Volvo",180,12)
print("Vehicle Name:",school_bus.name,"Speed:",school_bus.max_speed,"Milleage:",school_bus.milleage)
