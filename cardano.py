
from main import coefficients
from math import sqrt
from complex import *

def quadratic(a, b, c):
    return [(complex(-1, 0)*b+(b*b-4*a*c).squareRoot())/(complex(2, 0)*a), (complex(-1, 0)*b-(b*b-4*a*c).squareRoot())/(complex(2)*a)]

H = (coefficients[1])/3
G = coefficients[0]

print(H, G)

u, v = quadratic(complex(1, 0), complex(G, 0), complex(-(H**3), 0))

# k = 

answers = []

for i in range(3):
    currentRoot = cbrt(u)