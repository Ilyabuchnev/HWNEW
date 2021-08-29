from itertools import cycle, count
print('Для генерации следующего повторения необходимо нажать Enter, для выхода',
     'нажмите w')
a = input('Введите список, разделяя элементы пробелом: ').split()
i_ = cycle(a)
b = None

while b !='w':
    print(next(i_), end='')
    b = input()

# print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего необходимо нажать Enter',
#       'для выхода нажмите Q')
# for i in count(int(input('Введите стартовое число'))):
#     print(i, end=' ')
#     quit = input()
#     if quit =='q':
#         break