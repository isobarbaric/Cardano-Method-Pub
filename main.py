
from depress_cubic import *
from complex import *
from cardano import *

# list indices 'i' map directly to a_i notation 
coefficients = [int(i) for i in input("Enter the cubic polynomial's coefficients in order of increasing degree separated by spaces. Any vanishing terms should be included with the coefficient zero.").split()]

u, v = quadratic(complex(1), complex(1), complex(1))
print(u, v)

# mention real coefficients only 

coefficients, H, G, shift = depressed_cubic(coefficients)

answers = cardano_method(H, G, shift)

print(answers)