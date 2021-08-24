def my_division(num1, num2):
    try:
        div = (num1 / num2)
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
    return div

result = my_division(int(input('Введите делимое: ')), int(input('Введите делитель: ')))
print(result)