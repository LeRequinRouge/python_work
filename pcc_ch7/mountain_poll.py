# empty dictionary
responses = {}

# flag for while loop exit
polling_active = True

while polling_active:
    name = input("\nEnter your name: ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response

    repeat = input("Any more responses? Type Yes/No: ")
    if repeat.title() == 'No':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

