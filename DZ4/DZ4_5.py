from functools import reduce

def mult_a(a, b):
    return a * b

a = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(mult_a, a))
