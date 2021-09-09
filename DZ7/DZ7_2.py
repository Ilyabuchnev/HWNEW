from abc import ABC, abstractmethod

class Atelier(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def material_rezult(self):
        return f'Затраченная ткаьи итого: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'


class Coat(Atelier):

    def material_rezult(self):
        return f'На пошив пальто затрачено ткани: {self.param / 6.5 + 0.5 :.2f}'

class Suit(Atelier):

    def material_rezult(self):
        return f'На пошив костюма затрачено ткани: {2 * self.param + 0.3 :.2f}'

coat = Coat(50)
suit = Suit(10)

print(coat.material_rezult())
print(suit.material_rezult())





