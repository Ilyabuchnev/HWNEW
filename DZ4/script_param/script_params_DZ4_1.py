from sys import  argv
def Z_P (arb_hour, bet_hour):
    a = int(input('Введите отработанное время в часах: '))
    b = int(input('Введите ставку в рублях: '))
    return (a * b) * 1.1

c = Z_P(int(argv[1]), int(argv[2]))
print(f'Зарплата сотрудника составляет: {c} руб.')


# C:\Users\Лиза\Desktop\HWNEW\DZ4>python script_param\script_params_DZ4_1.py 58 1200
