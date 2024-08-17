filename = "programming_poll_results.txt"
with open(filename, 'w') as file_object:
    file_object.write("This is the poll results for multiple users:" + "\n")

with open(filename, 'a') as file_object:
    poll_flag = True

    while poll_flag:
        user_input = input("Why do you like programming? OR enter 'quit' to exit: ")
        if user_input == 'quit':
            poll_flag = False
        else:
            file_object.write(user_input + "\n")