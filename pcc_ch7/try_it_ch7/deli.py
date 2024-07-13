# 2 lists, one filled with sandwich orders
# and another empty waiting to be filled
# with completed sandwiches
sandwich_orders = ['pastrami', 'philly', 'torpedo', 'pastrami', 'knuckle', 'pastrami']
finished_sandwiches = []

# out of pastrami 7-9
print("\nSorry, but we ran out of pastrami!")

# loop to remove all pastrami orders from list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# loop to move the order to complete
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"Finished {sandwich.title()} sandwich.")

print("\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich is ready for pickup.")



