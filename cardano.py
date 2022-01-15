
from main import coefficients
from math import sqrt

def quadratic(a, b, c):
    return [(-1*b+sqrt(b*b-4*a*c))/(2*a), (-1*b-sqrt(b*b-4*a*c))/(2*a)]

H = (coefficients[1])/3
G = coefficients[0]

print(H, G)

u, v = quadratic(1, G, -(H**3))

# k = 

answers = []

for i in range(3):
    currentRoot = cbrt(u)
