num = str(input('Введите число: '))
print(int(num) + int(''.join([num,num])) + int(''.join([num,num,num])))