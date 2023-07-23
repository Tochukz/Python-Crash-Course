from car import Car
from electric_car import ElectricCar as ECar

my_new_car = Car("Ford", "EcoSport", 2019)
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(43)
my_new_car.update_odometer(21)
my_new_car.increment_odometer(17)
my_new_car.increment_odometer(-10)
my_new_car.read_odometer()
print()

ecar = ECar('Tesla', 'ModelX', 2019)
print(ecar.get_descriptive_name())