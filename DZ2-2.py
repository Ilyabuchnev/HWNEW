import copy
a_list = [int(i) for i in input('Введите числа через пробел: ').split()]
b = copy.copy(a_list)
for i in range (1, len(b), 2):
    b[i - 1], b[i] = b[i], b[i - 1]
print(a_list)
print(b)
