from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Inherited from Restaurant class and adds additional methods."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'vanilla',
            'chocolate',
            'strawberry',
            'rocky road',
            'moose tracks',
            'americone dream',
            'sherbert',
        ]

    def show_flavors(self):
        print("Here are the ice cream flavors of this stand:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


manic_ice_cream = IceCreamStand('Manic', 'Frozen Dairy Treat')
manic_ice_cream.show_flavors()

