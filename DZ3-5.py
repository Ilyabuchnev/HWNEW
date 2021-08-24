# lst = [int(i) for i in input('Введите числа через пробел ').split()]
# sum = 0
# i = 0
# while i < len(lst):
#         sum += lst[i]
#         i += 1
# print(sum)
num = 0
try:
    while num != "w":
        for i in map(int(input('Для выхода введите "w" или введите число через пробел: '))).split():
            num += i
            print(num)
except ValueError:
                print(num)