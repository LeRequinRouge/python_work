# List with multiples of 3s
# concise version using comprehensive
threes_list = [value for value in range(3, 31, 3)]
print(threes_list)

# for loop to print the list down the line
for value in threes_list:
    print(value)

# less concise version
threes_list = []
for value in range(3,31,3):
    threes_list.append(value)
    print(value)

print(threes_list)