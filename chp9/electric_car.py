from car import Car

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self): 
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        if self.battery_size == 75: 
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315
        
        print(f"This car can go about {car_range} miles on full charge")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Electric cars do not have gas tanks")
