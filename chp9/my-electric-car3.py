from electric_car import * 
# This method is not recommended for two reasons. 
# First, it’s helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses.
# With this approach it’s unclear which classes you’re using from the module. 
# This approach can also lead to confusion with names in the file.

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
