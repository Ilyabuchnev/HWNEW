def add_data(f, l, y, c, e, p):
     data = [f, l, y, c, e, p]
     return data
strin = add_data(input('Введите Имя: '), input('Введите Фамилию: '),\
                 int(input('Введите год рождения: ')),input('Введите город проживания: '),\
                 input('Введите email: '), input('Введите телефон: '))
for i in range(len(strin)):
    print(strin[i], end=' ')

