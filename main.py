
import numpy as np

from depress_cubic import *
from complex import *
from cardano import *
from covid import *
from generator import *
import time

all_exceptions = []
total_faults = 0 # faults = exceptions + difference in decimal places 
maxi_difference = 0

def run_tests():
    generate_data()
    num_faults = 0
    with open('tests.txt', 'r') as db:
        maxiDiff = 0
        for i in range(1, num_tests+1): # replace 10 with number of tests
            coeff = [int(i) for i in db.readline().replace('[', '').replace(']', '').split(', ')]
            roots = [Complex(i.real, i.imag) for i in (np.roots(coeff)).tolist()] 
            coeff, H, G, shift = depressed_cubic(coeff[::-1])
            try:
                answers = cardano_method(H, G, shift)
            except Exception as e:
                num_faults += 1
                all_exceptions.append(str(e.__class__.__name__))
                continue
            ok = True
            answers.sort()
            roots.sort()
            for i in range(3):
                print(answers[i], roots[i])
                if abs(answers[i].real-roots[i].real) > 1e-4:
                    ok = False
                    maxiDiff = max(maxiDiff, abs(answers[i].real-roots[i].real))
                if abs(answers[i].imaginary-roots[i].imaginary) > 1e-4:
                    ok = False
                    maxiDiff = max(maxiDiff, abs(answers[i].imaginary-roots[i].imaginary))
            ok = True
            num_faults += 1-ok
    return [num_faults, maxiDiff]

num_datasets = 1

start = time.time()
for i in range(num_datasets):
    start_local = time.time()
    more_faults, local_maximumDiff = run_tests()
    total_faults += more_faults
    maxi_difference = max(local_maximumDiff, maxi_difference)
    end_local = time.time()
    print(f'{end_local-start_local} seconds elapsed...')
    print()
end = time.time()

print(f'{end-start} seconds were taken to run {num_datasets*10000} total tests. The success rate at obtaining the correct roots with 4 decimal places was {(1-(total_faults/(num_datasets*10000)))*100}%.')