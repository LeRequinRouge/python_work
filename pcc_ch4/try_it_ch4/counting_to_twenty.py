# simple program that counts to twenty

# attempting the comprehensive version
count = [value for value in range(1, 21)]
print(count)

# less concise version
count = []
for value in range(1, 21):
    count.append(value)

print(count)

# down the line version
for value in range(1, 21):
    print(value)
