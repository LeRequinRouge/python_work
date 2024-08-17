filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write(f"I love the number {str(1000)}.\n")
    file_object.write(f"I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding the meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")