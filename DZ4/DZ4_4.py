from random import randint

a = [randint(1, 14) for _ in range(14)]
b = []
for i in a:
    if a.count(i) == 1:
        print(i, end=' ')
        b.append(i)
