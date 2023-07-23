"""A class that can be used to represent a car."""

class Car: 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self): 
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, new_milage):
        if self.odometer_reading > new_milage: 
            print("You can't roll back the milage!")
            return
        self.odometer_reading = new_milage

    def increment_odometer(self, milage): 
        if (milage < 0):
            print("You can increment the milage by negative value")
            return
        self.odometer_reading += milage
    
    def fill_gas_tank(self):
        print("Gas tank is now filled!")




