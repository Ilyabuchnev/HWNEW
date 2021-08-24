def my_func(num1, num2, num3):
    sum_my_func = int(num1 + num2 + num3) - min(num1, num2, num3)
    return sum_my_func
result = my_func(100, 200, 20)
print(result)