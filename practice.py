class Vehicle:
    def __init__(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def __str__(self):
        return f"This vehicle is {self.color}."    
    
class Car(Vehicle):
    def __init__(self, color,has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires
    def __str__(self):
        return f"{super()._str_()}\nHas winter tires: {self.has_winter_tires}"    
    
class Truck(Vehicle):
    def __init__(self,has_trailer=False):
        super().__init__(self)
        self.has_trailer = has_trailer
    def __str__(self):
        base_str = super().__str__()
        trailer_info = f"Has trailer: {self.has_trailer}"
        return f"{base_str}\n{trailer_info}"
    
class Garage:
    def __init__(self):
        self.parked_vehicle = None
    def setVehicle(self, parked: Vehicle):
        self.parked_vehicle = parked
    def __str__(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle}"
        else:
            return "The garage is empty."   
        
class GarageTester:
    @staticmethod
    def getExample():
        # Create a Truck object
        truck = Truck(make="Ford", model="F-150", has_trailer=False, color="black") 
        # Create a Garage object
        garage = Garage()        
        # Park the Truck in the Garage
        garage.setVehicle(truck)
        return garage        
    
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"Customer Name: {self.name}, Address: {self.address}"    