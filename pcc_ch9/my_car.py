from car import Car
from electric_car import ElectricCar

my_new_car = Car('toyota', 'tacoma', 2010)
print(my_new_car.get_descriptive_name())

my_ev = ElectricCar('chevy', 'volt', 2020)
print(my_ev.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_ev.odometer_reading = 50
my_ev.read_odometer()