from car import Car
from electric_car import ElectricCar

my_ev = ElectricCar('rivian', 'r1s', 2023)

print(my_ev.get_descriptive_name())
my_ev.battery.describe_battery()
my_ev.battery.get_range()