# the sort() method arranges objects in the list in alphabetical order
# note: sort() permanently changes the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort(reverse=True) arranges objects in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

# sorted() temporarily changes the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is a backwards sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# reverse() method reverses the contents of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

cars.reverse()
print(cars)

# you can find the length of the list using len(list) method
print(len(cars))