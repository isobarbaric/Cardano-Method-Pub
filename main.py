from depress_cubic import *
from complex import *
from cardano import *

coeff = covid_graph()
coeff.reverse()

coeff, H, G, shift = depressed_cubic(coeff)

print(coeff)

answers = cardano_method(H, G, shift)

for root in answers:
    print(root)
