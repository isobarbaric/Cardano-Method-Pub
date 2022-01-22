from depress_cubic import *
from complex import *
from cardano import *

# list indices 'i' map directly to a_i notation 
coeff = [int(i) for i in input("Enter the cubic polynomial's coefficients in order of increasing degree separated by spaces. Any vanishing terms should be included with the coefficient zero.\n").split()]

# real coefficients only 

coeff, H, G, shift = depressed_cubic(coeff)

answers = cardano_method(H, G, shift)

for root in answers:
    print(root)
