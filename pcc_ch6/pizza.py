# storing a list inside a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize the order
print(f"You ordered a {pizza['crust']} crust pizza "
      f"with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)