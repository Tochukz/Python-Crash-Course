import electric_car 

battery = electric_car.Battery()
battery.upgrade_battery()

my_tesla = electric_car.ElectricCar('Tesla', 'ModelX', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
my_tesla.battery = battery
my_tesla.battery.get_range()
