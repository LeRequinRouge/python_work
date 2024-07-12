# boolean flag to stop the while loop
order_ready = True

# while user is still inputting topping values, run the loop
while order_ready == True:
    topping = input("Please select a pizza topping or type 'quit' to exit: ")

    # boolean flag trip that exits the loop
    if topping == 'quit':
        order_ready = False
        print("\nYour pizza will be ready, soon!")
    # print the desired topping
    else:
        print(f"\nAdded {topping.title()} to your pizza!")
