# storing more dictionaries in a list
# this time, the dictionaries represent pets
tux = {
    'name': 'tux',
    'animal': 'cat',
    'owner': 'drew',
}

oli = {
    'name': 'oli',
    'animal': 'dog',
    'owner': 'leah',
}

sol = {
    'name': 'sol',
    'animal': 'bearded dragon',
    'owner': 'avi',
}

pets = [tux, oli, sol]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['animal']} "
          f"and belongs to {pet['owner'].title()}.")