# def my_func (x, y):
#     way = int(x)**int(y)
#     return way
# degree = my_func(x= float(input("Введите действительное положительное число: ")),\
#                                     y = input("Введите целое отрицательное число: "))
# print(degree)

def my_func (x, y):
    num = 1
    for i in range(abs(y)):
        num *= x
    if y >= 0:
        return num
    else:
        return 1/num
print(my_func(float(input("Введите действительное положительное число: ")),\
                                      int(input("Введите целое отрицательное число: "))))


