from math import factorial
from itertools import count

def gen_factor():
    for i in count(1):
        yield factorial(i)
gener = gen_factor()
x =0

for i in gener:
    if x == 15:
        break
    else:
        x += 1
        print(f"F {x} = {i}")