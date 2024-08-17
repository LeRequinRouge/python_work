# this program takes user input via while loop
# for a continuous entry of guest names that
# are stored in an external file.
filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    guest_flag = True
    while guest_flag:
        user_input = input('Enter guest name OR "quit" to exit: ')
        if user_input == "quit":
            guest_flag = False
        else:
            file_object.write(user_input + '\n')