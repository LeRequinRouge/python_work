# creates an empty list
squares = []

# for loop of the range 1-10 (stops at 11)
for value in range(1, 11):
    # new variable is the value in range to the power of 2
    square = value ** 2
    # variable is stored in the squares list
    squares.append(square)
    # squares.append(value**2) is a more concise way of writing

print(squares)

# simple statistics with lists of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# comprehension list identical but more concise with beginning code
square = [value**2 for value in range(1, 11)]
print(squares)