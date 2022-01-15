
class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary 
        return complex(real_part, imaginary_part)
    
    def __sub__(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary 
        return complex(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.real*other.real + self.imaginary*other.imaginary
        imaginary_part = self.real*other.imaginary + self.imaginary*other.real
        return complex(real_part, imaginary_part)
        
    def __truediv__(self, other):
        div_by = (other.real ** 2) - (other.imaginary ** 2)
        print(div_by)
        if self.imaginary > 0:
            real_part = (complex(self.real, 0)*complex(other.real, -1*other.imaginary))/div_by
            imaginary_part = (complex(0, self.imaginary)*complex(other.real, -1*other.imaginary))/div_by
        else:
            real_part = (complex(self.real, 0)*complex(other.real, -1*other.imaginary))/div_by
            imaginary_part = (complex(0, self.imaginary)*complex(other.real, -1*other.imaginary))/div_by
            
    def __str__(self):
        sign = '+'
        if (self.imaginary < 0):
            sign = '-'
        return ("{}" + sign + "{}i").format(self.real, abs(self.imaginary))

p1 = complex(1, -2)
p2 = complex(3, 1)
print(p1/p2)