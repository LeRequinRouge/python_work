# note: one element tuples require a trailing comma
# e.g. my_t = (3,)
dimensions = (200, 50)
print(dimensions[0], dimensions[1])

# looping through a tuple
for dimension in dimensions:
    print(dimension)

# redefining a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)