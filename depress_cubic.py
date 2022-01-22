
def depressed_cubic(coeff):
    shift = coeff[2]/(3*coeff[3])
    H = (coeff[1]-(coeff[2]*coeff[2])/(3*coeff[3]))/3
    G = ((2*(coeff[2] ** 3))/(27*(coeff[3] ** 2))) - (coeff[1]*coeff[2])/(3*coeff[3]) + coeff[0]
    H /= coeff[3]
    G /= coeff[3]
    a_3 = 1
    a_2 = 0
    a_1 = (3*H)/coeff[3]
    a_0 = G/coeff[3]
    return [[a_0, a_1, a_2, a_3], H, G, shift]