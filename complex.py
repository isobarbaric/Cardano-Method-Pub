
import math

class Complex:

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real*other, self.imaginary*other)
        else:
            real_part = self.real*other.real - self.imaginary*other.imaginary
            imaginary_part = self.real*other.imaginary + self.imaginary*other.real
            return Complex(real_part, imaginary_part)
    
    def __rmul__(self, other): 
        # one integer*Complex numbers will come to here since all other cases are dealt with by the __mul__ function
        return self.__mul__(other)

    def __pow__(self, number): # number > 0 
        if (number == 0):
            return Complex(1, 0)
        else:
            currentNumber = self
            for i in range(number-1):
                currentNumber *= self
                # currentNumber = self * currentNumber
        return currentNumber

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary 
        return Complex(real_part, imaginary_part)
    
    def __sub__(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary 
        return Complex(real_part, imaginary_part)

    def __init__(self, real, imaginary=None):
        self.real = real
        if imaginary is None:
            self.imaginary = 0
        else:
            self.imaginary = imaginary
        self.absValue = math.sqrt((self.real ** 2) + (self.imaginary ** 2))

    def __repr__(self):
        return f"{self.real}+{self.imaginary}i"

    def __lt__(self, other):
        return self.absValue < other.absValue

    def __truediv__(self, other):
        numerator = self*Complex(other.real, -1*other.imaginary)
        denominator = (other.real ** 2) + (other.imaginary ** 2)
        return Complex(numerator.real/denominator, numerator.imaginary/denominator)

    def __str__(self):
        if self.imaginary == 0:
            return str(self.real)
        sign = '+'
        if (self.imaginary < 0):
            sign = '-'
        return ("{}" + sign + "{}i").format(self.real, abs(self.imaginary))
        
    def __round__(self, num_digits=4):
        rev_real = round(self.real, num_digits)
        rev_imaginary = round(self.imaginary, num_digits)
        return Complex(rev_real, rev_imaginary)

    def root(self, value=2.0):
        k = self.absValue  # sin x = a/k, cos x = b/k
        x = math.degrees(math.acos(self.real/k))
        # assertions to ensure that the correct number has been identified (assertions messing everything up)
        # assert math.isclose(math.cos(math.radians(x)), self.real/k)
        # assert math.isclose(math.sin(math.radians(x)), self.imaginary/k)
        x /= value # since square rots is basically having the angle 
        r = k**(1/float(value)) # to get the cube root of the magnitude of the Complex number 
        rev_real = r*math.cos(math.radians(x)) 
        rev_imaginary = r*math.sin(math.radians(x))
        return Complex(rev_real, rev_imaginary)