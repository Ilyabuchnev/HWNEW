class Cell:
    def __init__(self, param):
        self.param = int(param)

    def __add__(self, other):
        return self.param + other.param

    def __sub__(self, other):
        return (self.param - other.param) if (self.param - other.param) > 0 else 'None'

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        return round(self.param / other.param)

    def make_order(self, row):
        rez = ''
        for i in range(int(self.param / row)):
            rez += '*' * row + '\n'
        rez += '*' * (self.param % row) + '\n'
        return rez
cell1 = Cell(20)
cell2 = Cell(10)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell2.make_order(5))