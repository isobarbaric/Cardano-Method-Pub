
from main import coefficients
from math import sqrt
from complex import *

def quadratic(a, b, c):
    return [(complex(-1, 0)*b+(b*b-complex(4, 0)*a*c).squareRoot())/(complex(2, 0)*a), (complex(-1, 0)*b-(b*b-complex(4, 0)*a*c).squareRoot())/(complex(2, 0)*a)]

H = complex((coefficients[1])/3, 0)
G = complex(coefficients[0], 0)

print(H, G)

u, v = quadratic(complex(1, 0), complex(G, 0), complex(-(H**3), 0)) # u, v are data members of type complex

# u, v = quadratic(complex(1, 0), complex(2, 0), complex(9, 0)) 

first = u.cubeRoot()
second = -H/u.cubeRoot()

omega, omega_sq = quadratic(complex(1, 0), complex(1, 0), complex(1, 0))

answers = []

for i in range(3):
    currentRoot = (omega ** i)*(first) + (omega ** (3-i))*(second)
    answers.append(currentRoot)

print(answers)