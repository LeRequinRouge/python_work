starting_number = 2

import imports_functions
new_number = imports_functions.power_of_two(starting_number)
print(new_number)

from imports_functions import power_of_two
new_number = power_of_two(new_number)
print(new_number)

from imports_functions import power_of_two as pot
new_number = pot(new_number)
print(new_number)

# 'if' is a keyword so it cannot be used as an alias
import imports_functions as imf
new_number = imf.power_of_two(new_number)
print(new_number)

from imports_functions import *
new_number = power_of_two(new_number)
print(new_number)