class My_Exc(Exception):
    def __init__(self):
        pass


class My_list:
    def __init__(self):
        self.a = []

    def My_list_value(self):
        global х
        while True:
            try:
                try:
                    х = int(input('Введите числа: '))
                    ex = input(f'Добавляется "{х}" в список. Хотите продолжить? y/n: ').lower()
                    self.a.append(х)
                    if ex == 'n':
                        print(self.a)
                        break
                except ValueError:
                    raise My_Exc
            except My_Exc:
                ex = input(f"Вы ввели не число! Хотите продолжить? y/n: ").lower()
                if ex == 'n':
                    print(self.a)
                    break
                else:
                    self.My_list_value()


a = My_list()
a.My_list_value()