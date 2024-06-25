# List alteration
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# append() method adds content to the back of the list
motorcycles.append('honda')
print(motorcycles)

# resets the list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# insert() method adds an object to given index then shifts other data
motorcycles.insert(0, 'ducati')
print(motorcycles)

# del statement can remove objects
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# pop() method removes an object from the back of the list but still allows you to use the value
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned_motorcycle = motorcycles.pop()
message = f"The last motorcycle I owned was a {last_owned_motorcycle.title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.append('ducati')

# can use the remove() method to delete by-name objects from a list
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
message = (f"\nA {too_expensive.title()} is too expensive for me.")
print(message)

# off-by-one example
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])

# again... [-1] accesses the last item in the list
# note: this will return with an error on an empty list
# motorcycles = []
print("\n", motorcycles[-1])