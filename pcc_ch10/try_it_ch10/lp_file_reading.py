# program that reads a file and manipulates/prints the data 3 different ways
filename = '/Users/Cuda/PycharmProjects/python_work/pcc_ch10/text_tests/learning_python.txt'

lines_list = []
c_lines_list = []

with open(filename) as file_object:
    lines = file_object.readlines()

# first display by reading the entire file
print(lines)

# second display by looping through the data
for line in lines:
    print(line.rstrip())
    lines_list.append(line.rstrip())
    c_lines_list.append(line.replace('Python', 'C').rstrip())

# third display utilizing a list
print(lines_list)

# learning C portion 10-2
print(c_lines_list)

