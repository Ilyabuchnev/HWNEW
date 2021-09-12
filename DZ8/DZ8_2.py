class MyException:
    def __init__(self, text):
        self.text = text


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def O_exception():
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))
        if b == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = a / b
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err

print(O_exception())