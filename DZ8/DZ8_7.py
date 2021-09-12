class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c1 = ComplexNum(10, 2)
c2 = ComplexNum(49, -41)
print(c1 + c2)
print(c1 * c2)