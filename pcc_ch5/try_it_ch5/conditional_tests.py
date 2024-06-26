# given conditional tests
car = 'subaru'
print("Is car == 'subaru'? I predict True...")
print(car == 'subaru')

print("Is car != 'audi'? I predict False...")
print(car == 'audi')

# created conditional tests
favorite_number = 6

print("Is my favorite number 6? I think so...")
print(favorite_number == 6)

print("What about 8? I think not...")
print(favorite_number == 8)

# more conditional tests
# 1: equality and inequality with strings
musical_instrument = 'piano'
print("Is this instrument a piano?")
print(musical_instrument == 'piano')

print("How about a trombone?")
print(musical_instrument == 'trombone')

# 2: lower method testing
famous_actor = 'Morgan Freeman'
print(famous_actor == 'morgan freeman')
print(famous_actor.lower() == 'morgan freeman')

# 3: numerical testing
base = 66
side = 7

print("Is the base 66?")
print(base == 66)
print("Is the side 4?")
print(base == 4)

if base > 77:
    print("HeheHAHA")
if base >= 55:
    print("This is bigger than that.")
if side < 10:
    print("Okay, it's working.")
if side <= 1:
    print("I get it, really!")

# 4: and/or keyword testing
if base == 66 and side == 6:
    print("This is a very odd shape!")

if base == 44 or side == 7:
    print("It's thundering pretty heavily outside...")

# 5: In a list testing
my_organs = ['heart', 'liver', 'kidney']

for organ in my_organs:
    if organ == 'liver':
        print("Alcohol hasn't got me yet!")

# 6: Not in a list testing
organ = 'brain'
if organ not in my_organs:
    print("OOF... I always knew.")