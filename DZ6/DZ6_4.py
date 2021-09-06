class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def get(self):
        return f'Go {self.name}'

    def stop(self):
        return f'\nStop {self.name}'

    def turn(self, direction):
        return f'\n{self.name} turned {direction}'

    def show_speed(self):
        return f'\nspeed ={self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревыешение скорости {self.speed}'
        else:
            return f'Скорость в рамках лимита - {self.name}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревыешение скорости{self.speed}'
        else:
            return f'Скорость в рамках лимита - {self.name}'


class PoliceCar(Car):
    pass

w = WorkCar('Gaz', 35, 'White', False)
print('WorkCar:\n' + w.get(), w.show_speed(), w.turn('right'), w.stop())

s = SportCar('Маруся', 200, 'Blue', False)
print('SportCar:\n' + s.get(), s.show_speed(), s.turn('left'), s.stop())

t = TownCar('Lada', 78, 'Green', False)
print('TownCar:\n' + t.get(), t.show_speed(), t.turn('left'), t.turn('right'), t.stop())

p = PoliceCar('Toyota', 140, 'Gras', True)
print('PoliceCar:\n' + w.get(), w.show_speed(), w.turn('right'), w.stop())