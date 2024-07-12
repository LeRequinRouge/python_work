seating = input("How many people in your party? ")
seating = int(seating)

if seating > 8:
    print("We're sorry, but you will have to wait 30 minutes for a table.")
else:
    print("Your table is ready!")