# intro to the range() function
# prints everything but the end of the range
for value in range(1, 5):
    print(value)
# 1, 2, 3, 4 is printed... range(1, 6) is required to print 5

# output includes 0 through 5
for value in range(6):
    print(value)

# utilizing the list() function
numbers = list(range(1, 6))
# [1, 2, 3, 4, 5] is the result
print(numbers)

# the range function can take a third argument to skip sections
even_numbers = list(range(2, 11, 2))
# [2, 4, 6, 8, 10] is the result
print(even_numbers)
