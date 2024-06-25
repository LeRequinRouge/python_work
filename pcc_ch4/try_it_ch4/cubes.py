# This program creates a list of cubed integers from 1-10
cubed_list = [value**3 for value in range(1, 11)]
print(cubed_list)

# down the line version to print
for value in cubed_list:
    print(value)

# less concise version
cubed_list = []
for value in range(1, 11):
    cubed_list.append(value**3)
    print(value)

print(cubed_list)