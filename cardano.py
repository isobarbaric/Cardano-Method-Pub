
from math import sqrt
from complex import *

def quadratic(a, b, c):
    return [(-1*b+(b*b-4*a*c).root())/(2*a), (-1*b-(b*b-4*a*c).root())/(2*a)]

def mod(value, shift):
    return round(value - shift)

def cardano_method(H, G, shift):
    # u, v are data members of type complex
    u, v = quadratic(complex(1), complex(G), complex(-(H ** 3))) 
    # print(u, v)
    first = round(u.root(3))
    # print(first)
    second = round(complex(-H)/u.root(3))
    # print(second)
    omega, omega_sq = quadratic(complex(1), complex(1), complex(1))
    # print(omega)
    withoutShift = [round(first+second), round(omega*first+omega_sq*second), round(omega_sq*first+omega*second)]


    # answers = [mod(i, shift) for i in withoutShift]

    answers = withoutShift

    for i in range(3):
        print(answers[i])

    return answers 