import random

lottery = (
    'd',
    't',
    'u',
    'q',
    'z',
    1,
    6,
    10,
    23,
    36,
    40,
    68,
    81,
    88,
    94
)

winning_values = []
my_ticket = []
count = 0


def pull_values(tuple, winning_list):
    del winning_list[:]
    for value in range(4):
        winning_list.append(random.choice(tuple))


def print_values(winning_list):
    for value in winning_list:
        print(value)


pull_values(lottery, winning_values)
print_values(winning_values)

while my_ticket != winning_values:
    pull_values(lottery, my_ticket)
    count += 1

print(f"You won the lottery after pulling {count} tickets!")

