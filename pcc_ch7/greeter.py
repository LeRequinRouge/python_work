# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# more user input practice involving numbers
age = input("How old are you? ")
age = int(age)

if age < 18:
    print("You're too young to be here...")
else:
    print("Welcome, adult!")