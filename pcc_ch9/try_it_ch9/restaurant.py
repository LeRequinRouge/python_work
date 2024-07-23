class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Here we serve {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!\n")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers


restaurant1 = Restaurant("Del Taco", "Mexican Fastfood")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("BJ's", "Brewhouse")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("Outback", "Steakhouse")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

# 9-4 number served attribute modification
restaurant4 = Restaurant("Islands", "Tropical Fusion")
print(restaurant4.number_served)
restaurant4.number_served = 10
print(restaurant4.number_served)

# attribute modification via method
restaurant4.set_number_served(15)
print(restaurant4.number_served)

# attribute modification via incrementation
restaurant4.increment_number_served(5)
print(restaurant4.number_served)

