# this program polls users for dream vacation spots
# utilizing looping through dictionaries
pollers = {}

# flag to stop the while loop once set to false
poll_flag = True

while poll_flag:
    name = input("Enter your name to start the poll: ")
    response = input("What place would you like to go"
                     " for a dream vacation? ")

    pollers[name] = response

    repeat = input("Anyone else taking the poll? y/n: ")

    if repeat == 'n':
        poll_flag = False

for name, response in pollers.items():
    print(f"\n{name} would like to go to {response}.")