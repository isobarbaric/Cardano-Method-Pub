
from math import sqrt
from complex import *

def quadratic(a, b, c):
    return [(-1*b+(b*b-4*a*c).root())/(2*a), (-1*b-(b*b-4*a*c).root())/(2*a)]

def cardano_method(H, G, shift):
    u, v = quadratic(Complex(1), Complex(G), Complex(-(H ** 3))) 
    first = u.root(3)
    second = Complex(-H)/u.root(3)
    omega, omega_sq = [round(i) for i in quadratic(Complex(1), Complex(1), Complex(1))]
    withoutShift = [first+second, omega*first+omega_sq*second, omega_sq*first+omega*second]
    answers = [round(i-Complex(shift)) for i in withoutShift]
    return answers 

