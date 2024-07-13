# positionally passed arguments
# order of parameters matters
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# keyword passed arguments
# order does not matter, output is the same
describe_pet(animal_type='cat', pet_name='skittles')


# default parameter for pet type is set to 'dog'
def default_pet(pet_name, animal_type='dog'):
    """Display information about a pet using default value(s)"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# the pet type parameter can be omitted
default_pet(pet_name='velcro')
default_pet('rowdy')

# NOTE: default values must be pushed to the furthest
# parameter past all values that are not default