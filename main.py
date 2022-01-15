
from depress_cubic import modify

coefficients = [int(i) for i in input("Enter the cubic polynomial's coefficients in order of increasing degree separated by spaces. Any vanishing terms should be included with the coefficient zero.").split()]
# list indices 'i' map directly to a_i notation 

if (coefficients[2] != 0):
    coefficients = modify(coefficients)

