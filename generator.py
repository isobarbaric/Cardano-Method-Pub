
import random 

lower_limit = 1
upper_limit = 10

num_tests = 10000

tests = []

def generate_data():
    for i in range(num_tests): 
        coeff = [] # in order a_n, a_{n-1}, ...
        for i in range(4):
            coeff.append(random.randint(lower_limit, upper_limit))
        tests.append(coeff)

    with open('tests.txt', 'w') as db:
        for data in tests:
            db.write("%s\n" % data)
    
    tests.clear()