import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

    def roll_it(self, rolls):
        print(f"{self.sides}-sided die rolled {rolls} times:")
        for attempts in range(rolls):
            print(Die.roll_die(self))
        print('\n')


# standard 6-sided die rolled 10 times.
standard_die = Die()
Die.roll_it(standard_die, 10)

# 10-sided die rolled 10 times.
pentagonal_die = Die(10)
Die.roll_it(pentagonal_die, 10)

# 20-sided die rolled 10 times.
icosahedron_die = Die(20)
Die.roll_it(icosahedron_die, 10)

