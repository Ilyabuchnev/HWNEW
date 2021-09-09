class Matrix:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        for row in self.val:
            for i in row:
                print(f"{i:3}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.val)):
            for i_2 in range(len(other.val[i])):
                self.val[i][i_2] = self.val[i][i_2] + other.val[i][i_2]
        return Matrix.__str__(self)

mc = Matrix([[3, 5, 1], [2, 7, 6], [9, 4, 1]])
mc2 = Matrix([[2, 7, 3], [4, 9, 5], [15, 24, 71]])
print(mc.__add__(mc2))




