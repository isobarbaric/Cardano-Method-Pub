
from main import coefficients
from math import sqrt
from complex import *

def quadratic(a, b, c):
    return [(complex(-1, 0)*b+(b*b-complex(4, 0)*a*c).squareRoot())/(complex(2, 0)*a), 
    (complex(-1, 0)*b-(b*b-complex(4, 0)*a*c).squareRoot())/(complex(2, 0)*a)]

shift = complex(coefficients[2]/(3*coefficients[3]), 0)

# this stuff should be calculated by the complex.py function and simply returned to this file 
H = (coefficients[1]-(coefficients[2] ** 2)/(3*coefficients[3]))/3
G = (2*(coefficients[2] ** 3))/(27*(coefficients[3] ** 2)) - (coefficients[1]*coefficients[2])/(3*coefficients[3]) + coefficients[0]

# print(H, G)

# u, v are data members of type complex
u, v = quadratic(complex(1, 0), complex(G, 0), complex(-(H ** 3), 0)) 
# print(u, v)

first = complex.round(u.cubeRoot())
# print(first)
second = complex.round(complex(-H, 0)/u.cubeRoot())
# print(second)

omega, omega_sq = quadratic(complex(1, 0), complex(1, 0), complex(1, 0))

answers = []

# print(first, second)
# print(omega*first, omega_sq*second)
# print(omega_sq*first, omega*second)
other = [first+second, complex.round(omega*first)+complex.round(omega_sq*second), complex.round(omega_sq*first)+complex.round(omega*second)]

def mod(value):
    return (value - shift)

rev = [mod(i) for i in other]

for i in range(3):
    print(rev[i])