print("Welcome to Slippery Snake Cinema!")

# flag set to true to start a loop
ticket_flag = True
ticket_cost = 0

# loop to obtain user input for age
# to determine movie ticket price
while ticket_flag:
    print("\nType '0' to exit the program.")
    customer_age = int(input("Please enter the age"
                             " of the movie goer: "))

    # user may enter 0 to exit the loop
    if customer_age == 0:
        break

    elif customer_age < 3 and customer_age > 0:
        print(f"\nThe little one watches for free! "
              f"\n${ticket_cost} due.")

    elif customer_age >= 3 and customer_age <= 12:
        ticket_cost = 10
        print(f"\nEnjoy the movie, child!"
              f"\n${ticket_cost} due.")

    elif customer_age > 12:
        ticket_cost = 15
        print(f"\nHope you like the movie!"
              f"\n${ticket_cost} due.")

    # an additional way out of the loop
    # by taking user input and setting
    # the loop flag to false
    user_repeat = input("\nWould you like to enter another"
                        " movie goer? y/n: ")
    if user_repeat == 'n':
        ticket_flag = False









