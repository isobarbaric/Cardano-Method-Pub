
from cmath import sinh
import math

class complex:
    
    def squareRoot(self, value = None): # complex part is going to be zero, meant for quadratic function only
        if value == None: # to take square roots of complex numbers and then return them 
            value = self.real
            if (value >= 0):
                return complex(math.sqrt(value), 0)
            else:
                return complex(0, math.sqrt(-1*value))
        else: # to take square roots of regular numbers 
            if (value >= 0):
                return math.sqrt(value)
            else:
                return math.sqrt(-1*value)

    def __pow__(self, number):
        if (number == 0):
            return complex(1, 0)
        else:
            currentNumber = self
            for i in range(number-1):
                currentNumber *= self
        return currentNumber

    # included before any other functions because used to initialize class object 

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.absValue = self.squareRoot((self.real*self.real) + (self.imaginary*self.imaginary))
    
    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary 
        return complex(real_part, imaginary_part)
    
    def __sub__(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary 
        return complex(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.real*other.real - self.imaginary*other.imaginary
        imaginary_part = self.real*other.imaginary + self.imaginary*other.real
        return complex(real_part, imaginary_part)
        
    def __truediv__(self, other):
        numerator = self*complex(other.real, -1*other.imaginary)
        denominator = (other.real ** 2) + (other.imaginary ** 2)
        return complex(numerator.real/denominator, numerator.imaginary/denominator)

    def __str__(self):
        sign = '+'
        if (self.imaginary < 0):
            sign = '-'
        return ("{}" + sign + "{}i").format(self.real, abs(self.imaginary))

    # using DeMoivre's Theorem, the cube root of a complex number can easily be computed 
    def cubeRoot(self): # meant for complex numbers so imaginary part may not be zero 
        k = self.absValue  # sin x = a/k, cos x = b/k
        x = math.degrees(math.acos(self.real/k))
        # assertions to ensure that the correct number has been identified 
        assert math.isclose(math.cos(math.radians(x)), self.real/k)
        assert math.isclose(math.sin(math.radians(x)), self.imaginary/k)
        x /= 3 # since square rots is basically having the angle 
        r = k**(1/float(3)) # to get the cube root of the magnitude of the complex number 
        rev_real = r*math.cos(math.radians(x)) 
        rev_imaginary = r*math.sin(math.radians(x))
        return complex(rev_real, rev_imaginary)