
from complex import Complex
from math import sqrt

class CubicEquation:

    # constructor

    def __init__(self, coeff): 
        # assigning a copy of the cofficients to an attribute variable
        self.equation = coeff.copy()

        print(self.equation)

        # reversing the list of coefficients, and assigning a copy of that list to an attribute variable
        coeff.reverse()
        self.coefficients = coeff.copy()

        # declaring and initializing dummy variables for future use
        self.H, self.G, self.shift = -1, -1, -1
        self.answers = []

    def __depressed_cubic(self):
        # determining the shift variable 
        shift = self.coefficients[2]/(3*self.coefficients[3])

        # determining H and G as per the coefficients of the polynomial
        H = (self.coefficients[1]-(self.coefficients[2]*self.coefficients[2])/(3*self.coefficients[3]))/3
        G = ((2*(self.coefficients[2] ** 3))/(27*(self.coefficients[3] ** 2))) - (self.coefficients[1]*self.coefficients[2])/(3*self.coefficients[3]) + self.coefficients[0]
        H /= self.coefficients[3]
        G /= self.coefficients[3]

        # assigning revised coefficients based on earlier results
        a_3 = 1
        a_2 = 0
        a_1 = (3*H)/self.coefficients[3]
        a_0 = G/self.coefficients[3]

        # assigning the results of the  
        self.coefficients, self.H, self.G, self.shift = [[a_0, a_1, a_2, a_3].copy(), H, G, shift]

    @staticmethod
    def quadratic(a, b, c):
        # determining the roots of a quadratic equation given the coefficients a, b, c

        return [(-1*b+(b*b-4*a*c).root())/(2*a), (-1*b-(b*b-4*a*c).root())/(2*a)]

    def __cardano_method(self):
        # finding u, v from Cardano's Method using a call to the static quadratic method
        u, v = CubicEquation.quadratic(Complex(1), Complex(self.G), Complex(-(self.H ** 3))) 

        # determining the first partial root
        first = u.root(3)

        # determining the second partial root
        second = Complex(-self.H)/u.root(3)

        # getting the values of the two constants omega and omega_sq
        omega, omega_sq = [round(i) for i in CubicEquation.quadratic(Complex(1), Complex(1), Complex(1))]

        # determining the roots using the constants determined
        withoutShift = [first+second, omega*first+omega_sq*second, omega_sq*first+omega*second]
       
        # using list-comprehension to perform the necessary shift
        answers = [round(i-Complex(self.shift)) for i in withoutShift]

        return answers 

    def solve(self):
        # depressing the given cubic equation
        self.__depressed_cubic()

        # using Cardano's method to get the roots of the cubic equation
        self.answers = self.__cardano_method()

        return self.answers.copy()

    def __repr__(self):
        print(self.equation)
        info = ""
        if (self.equation[0] != 1):
            info += str(self.equation[0])
        info += "x^3 + "
        if (self.equation[1] != 1):
            info += str(self.equation[1])
        info += "x^2 + "
        if (self.equation[2] != 1):
            info += str(self.equation[2])
        info += "x + " + str(self.equation[3])
        return info 

a = CubicEquation([3, 2, 3, 1])
print(a)
print(a.solve())
