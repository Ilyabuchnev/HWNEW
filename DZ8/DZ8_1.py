class Data:
    def __init__(self, param_data):
        self.param_data = param_data

    @classmethod
    def type(cls, param_data):
        try:
            day, month, year = [int(i) for i in param_data.split('-')]
            if month == 2 and day < 29:
                return 'Есть такая дата!'
            else:
                raise ValueError
        except ValueError:
            return 'Указана неверная дата!'

    @staticmethod
    def valid(param_data):
        try:
            day, month, year = param_data.split('-')
            if month == 2 and day < 29:
                return 'Есть такая дата!'
            else:
                raise ValueError
        except ValueError:
                return 'Указана неправильная дата!'

print(Data.valid('20-05-1986'))
print(Data.type('22-02-1985'))