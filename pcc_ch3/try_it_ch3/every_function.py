# This program creates a list and then uses every function in ch. 3 on it.

# list of some basic fire emblem classes
my_list = ['cleric', 'brigand', 'monk', 'soldier', 'cavalier', 'fighter', 'shaman', 'mercenary',
           'knight', 'myrmidon', 'mage', 'archer', 'pirate', 'lord', 'nomad', 'pegasus rider', 'wyvern rider']

# length of the list
print(f"There's {len(my_list)} objects in this list.")

# print the original
print(my_list)
print("\n")

# print a temporary sorted version
print(sorted(my_list))
print("\n")

# print a temporary reverse order version
print(sorted(my_list, reverse=True))
print("\n")

# print a permanent reverse order without sorting
my_list.reverse()
print(my_list)
print("\n")

# print a permanent sorted version
my_list.sort()
print(my_list)
print("\n")

# print a permanent reverse order version
my_list.sort(reverse=True)
print(my_list)
print("\n")

# remove an object
my_list.remove('archer')
print(my_list)
print("\n")

# add an object to the end
my_list.append('archer')
print(my_list)
print("\n")

# pop the last object and us it
second_worst_class = my_list.pop().title()
print(f"The second worst class in FE is the {second_worst_class}.")
print(my_list, "\n")

# deletes the an object in the list
del my_list[0]
print(my_list, "\n")

# inserts an object anywhere in the list
my_list.insert(0, 'wyvern rider')
print(my_list)
