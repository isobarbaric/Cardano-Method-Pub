
#
import numpy as np
from matplotlib import pyplot as plt
#

from depress_cubic import *
from complex import *
from cardano import *
from covid import *

#
def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {ord}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y
#

#
coeff = [-4.5, 8.5, 3.5, 1.5]
coeff = [9722, -2445, 177, -2]
# print(coeff)
# print(np.roots(coeff[::-1]))
coeff, H, G, shift = depressed_cubic(coeff)
print(coeff[::-1])
# x = np.linspace(0, 60, 50)
# plt.plot(x, PolyCoefficients(x, coeff)) 
# plt.show()

answers = cardano_method(H, G, shift)

for root in answers:
    print(root)
#

# coeff = covid_graph()
# print(coeff)
# print(np.roots(coeff[::-1]))
# coeff, H, G, shift = depressed_cubic(coeff[::-1])
# print(coeff, H, G, shift)

# # test.reverse()
# # print(test[::-1]) # 

# #
# x = np.linspace(0, 60, 50)
# plt.plot(x, PolyCoefficients(x, coeff)) 
# # plt.xticks(np.arange(min(x), max(x)+1, 1.0))
# plt.show()
# #

# answers = cardano_method(H, G, shift)

# for root in answers:
#     print(root)