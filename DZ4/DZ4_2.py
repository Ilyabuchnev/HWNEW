# a = [254, 54, 98, 2, 77, 85, 3, 57, 14]
# b = []
# for i, elem in enumerate(a):
#     if a[i] > a[i-1]:
#         b.append(elem)
# print(a)
# print(b)

from random import randint
a = [randint(1, 254) ** 1 for _ in range(9)]
def func_a(x,y):
    for i in range(1, len(x), y):
        yield max(x[i : i + y])
print(list(func_a((a), 2)))
print(a)


