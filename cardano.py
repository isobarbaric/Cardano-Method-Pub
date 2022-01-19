
from math import sqrt
from complex import *

def quadratic(a, b, c):
    return [(-1*b+(b*b-4*a*c).root())/(2*a), (-1*b-(b*b-4*a*c).root())/(2*a)]

def cardano_method(H, G, shift):
    u, v = quadratic(complex(1), complex(G), complex(-(H ** 3))) 
    first = round(u.root(3))
    second = round(complex(-H)/u.root(3))
    omega, omega_sq = quadratic(complex(1), complex(1), complex(1))
    withoutShift = [round(first+second), round(omega*first+omega_sq*second), round(omega_sq*first+omega*second)]
    answers = [round(i-complex(shift)) for i in withoutShift]
    return answers 