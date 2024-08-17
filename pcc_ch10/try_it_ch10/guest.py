# this program takes user input to write guest
# names to an external file.
filename = "guest_name.txt"

with open(filename, 'w') as file_object:
    file_object.write(input("Enter your name: "))
    file_object.write("\n")

with open(filename, 'a') as file_object:
    file_object.write(input("Enter the name of a guest: "))
