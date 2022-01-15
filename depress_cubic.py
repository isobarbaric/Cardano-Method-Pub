
def modify(coefficients):
    mod = coefficients
    a_3 = mod[3]
    a_2 = 0
    a_1 = mod[1] - (mod[2] ** 2)/(3*mod[3])
    a_0 = (2*(mod[2] ** 3))/(27*(mod[3]) ** 2) - (mod[1]*mod[2])/(3*mod[3]) + mod[0]
    return [a_0, a_1, a_2, a_3]