from electric_car import ElectricCar, Battery

battery = Battery()
battery.upgrade_battery()

my_tesla = ElectricCar('Tesla', 'ModelX', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
my_tesla.battery = battery
my_tesla.battery.get_range()

