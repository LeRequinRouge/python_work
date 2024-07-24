class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This {self.make.title()} has {self.odometer_reading} miles on it.")

    # updating through a method,
    # + preventative measures for back-rolling the reading
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Fill the tank!"""
        print("Gas tank is now full!")


class Battery:
    """A simple attempt to represent a battery for an electric car."""

    def __init__(self, battery_size=75, travel_range=0):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self.travel_range = travel_range

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            travel_range = 260
        elif self.battery_size == 100:
            travel_range = 315

        print(f"This car can go about {travel_range} miles on a full charge.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# modifying an attribute's value through an instance
my_new_car.odometer_reading = 23

# modifying an attribute's value through a method
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# modifying an attribute's value through incrementing
my_used_car = Car('subaru', 'outback', 2015)
print("\n")
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()




