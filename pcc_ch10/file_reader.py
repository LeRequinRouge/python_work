# relative file extraction
with open('text_tests/test.txt') as test_object:
    testing = test_object.read()
print(testing.rstrip(), '\n')

# base 'in directory' file extraction
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip(), '\n')

# absolute pathing for file extraction
file_path = '/Users/Cuda/PycharmProjects/python_work/absolute_text/absolute_path.txt'
with open(file_path) as absolute_object:
    absolute = absolute_object.read()
    print(absolute, "\n")

# reading through lines of a file
filename = "pi_digits.txt"

print("Printing line data from another file:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())