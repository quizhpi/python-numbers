#
# Working With Numbers
#

# Import all functions from the math module
#  and no need to use the key word math in front of each function
#
# from math import *

# Another way to import the module but must follow by math.anyfunc() to access the functions
import math

# Convert number into string
num = 7
print(str(num))

# Get the absolute value of the variable
num = -5
print(abs(num))

# Using the builtin function pow() x^y
print(pow(5, 2))

# Get the greatest number with the function max()
print(max(99, 54))

# Get the smallest number with the function min()
print(min(100, 1))

# Using the round() function
print(round(1.99))

# Must import math in order to use the following function

# Round number down
print(math.floor(6.9))

# Round number up
print(math.ceil(6.9))

# square root of a number
print(math.sqrt(25))