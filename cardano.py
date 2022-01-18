
from main import coefficients
from math import sqrt
from complex import *

def quadratic(a, b, c):
    return [(complex(-1, 0)*b+(b*b-complex(4, 0)*a*c).squareRoot())/(complex(2, 0)*a), 
    (complex(-1, 0)*b-(b*b-complex(4, 0)*a*c).squareRoot())/(complex(2, 0)*a)]

# def raiseTo(base, exponent):
#     ans = complex(1, 0)
#     for i in range(exponent):
#         ans *= base
#     return ans

H = (coefficients[1]-(coefficients[2] ** 2)/(3*coefficients[3]))/3
G = (2*(coefficients[0] ** 3))/(27*(coefficients[3] ** 2)) - (coefficients[1]*coefficients[2])/(3*coefficients[3]) + coefficients[0]

# print(H, G)

u, v = quadratic(complex(1, 0), complex(G, 0), complex(-(H ** 3), 0)) # u, v are data members of type complex

# u, v = quadratic(complex(1, 0), complex(2, 0), complex(9, 0)) 

first = u.cubeRoot()
second = complex(-H, 0)/u.cubeRoot()

omega, omega_sq = quadratic(complex(1, 0), complex(1, 0), complex(1, 0))

answers = []

for i in range(3):
    currentRoot = ((omega ** i))*(first) + (omega ** (3-i))*(second)
    answers.append(currentRoot)

for i in range(3):
    print(answers[i])