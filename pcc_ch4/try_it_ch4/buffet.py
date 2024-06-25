# this program practices the creation and manipulation of a tuple
buffet_food = ('eggs', 'sausage', 'bacon', 'hash browns', 'biscuits & gravy')

for food in buffet_food:
    print(food.title())

# forced error:
# buffet_food[0] = 'ham'

# rewriting the tuple
buffet_food = ('pancakes', 'waffles', 'fruit', 'french toast', 'benedict')

for food in buffet_food:
    print(food.title())
