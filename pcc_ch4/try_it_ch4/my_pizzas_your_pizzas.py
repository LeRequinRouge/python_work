my_pizzas = ['pepperoni', 'meat lovers', 'supreme', 'white sauce']
your_pizzas = my_pizzas[:]

my_pizzas.append('honey prosciutto')
your_pizzas.insert(0, 'vegetarian')

print("My favorite pizzas are")
for pizza in my_pizzas:
    print(pizza)

print("\nYour favorite pizzas are")
for pizza in your_pizzas:
    print(pizza)
