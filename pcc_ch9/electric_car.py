from car import Car, Battery


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

    def upgrade_battery(self):
        """Upgrades battery from car class."""
        if self.battery.battery_size < 100:
            self.battery.battery_size = 100
        else:
            print("Battery size is already fully upgraded.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print("\n")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

# 9-9 battery upgrade portion
my_tesla.upgrade_battery()
my_tesla.battery.get_range()