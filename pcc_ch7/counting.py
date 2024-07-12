current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n")

# continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# avoiding infinite loops
print("\n")

x = 1
while x <= 5:
    print(x)
    # without this line, the loop would run forever
    x += 1