players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

# omitting the first number slices from beginning of the list
print(players[:5])

# similarly, omitting the second slices to the end of the list
print(players[2:])

# negative numbers can be used to reverse through the list
print(players[-3:])

message = "Here are the first three players on my team:"
print(message)
for player in players[0:3]:
    print(player.title())
