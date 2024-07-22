class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Here we serve {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!\n")


restaurant1 = Restaurant("Del Taco", "Mexican Fastfood")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("BJ's", "Brewhouse")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("Outback", "Steakhouse")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
