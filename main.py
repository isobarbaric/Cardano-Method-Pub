
from depress_cubic import *
from complex import *

# list indices 'i' map directly to a_i notation 
coefficients = [int(i) for i in input("Enter the cubic polynomial's coefficients in order of increasing degree separated by spaces. Any vanishing terms should be included with the coefficient zero.").split()]

# mention real coefficients only 

if (coefficients[2] != 0):
    coefficients = depressed_cubic(coefficients)



