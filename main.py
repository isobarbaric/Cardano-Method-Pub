

import random 
import json

lower_limit = 1
upper_limit = 750

num_tests = 10000

tests = {}

for i in range(num_tests): 
    real_part = random.randint(lower_limit, upper_limit)
    imaginary_part = random.randint(lower_limit, upper_limit)
    a = complex(real_part, imaginary_part)
    tests[str(a)] = str(a ** 3)

with open('tests.txt', 'w') as db:
    data = json.dumps(tests, indent = 4)
    db.write(data)