# import the file
import pizza
# importing a specific function
from pizza import make_pizza
# alias for imported function in case of name conflict
from pizza import make_pizza as mp
# can create an alias for entire function as well
import pizza as p
# can import all functions in a file using *
# but be careful with this approach on large
# modules that weren't written by you
from pizza import *

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# because we imported the specific function from pizza.py
# we can skip the pizza object dot notation and use
# it as if it was in this program.
make_pizza(20, 'jalapenos', 'bacon', 'sausage')

# we can also change the alias of the function
# in the event that the function name conflicts
# with existing functions in this program
mp(10, 'alfredo sauce', 'pineapple')

# concise version of object dot notation
p.make_pizza(30, 'bell peppers')