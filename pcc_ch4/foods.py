# copying lists
# make sure to use a slice [:] otherwise lists will point toward each other
# and be the same exact list subject to future modification.
# e.g. my_foods = friend_foods, appending a value to one affects both.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# proving separate lists
my_foods.append('ramen')
friend_foods.insert(1, 'hotdog')

print("My favorite foods are")
print(my_foods)

print("\nMy friend's favorite foods are")
print(friend_foods)