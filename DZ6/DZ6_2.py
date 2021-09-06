class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 40
        self.height = 3

    def mass(self):
        mass = self._length * self._width * self.weight * self.height / 100
        print(f'Для покрытия всего дорожного полотна неободимо {round(mass)} массы асфальта')


r = Road(3000, 16)
r.mass()