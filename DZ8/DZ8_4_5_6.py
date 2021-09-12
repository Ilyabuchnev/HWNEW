class Office_equipment:

    def __init__(self, model, price, country, color):
        self.model = model
        self.price = price
        self.country = country
        self.color = color
        self.items = {'Модель устройства': self.model, 'Цена за ед': self.price, 'Страна производитель': self.country, 'Цвет корпуса': self.color}

    def warehouse(self):
        try:
            model = input(f'Введите модель устройства: ')
            price = int(input(f'Введите цену за ед: '))
            country = input(f'Введите страну производства: ')
            color = input(f'Введите цвет порпуса: ')
            item = {'Модель устройства': model, 'Цена за ед': price, 'Страна производитель': country, 'Цвет корпуса': color}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(Office_equipment):
    pass


class shredder(Office_equipment):
    pass


class pamphleteer(Office_equipment):
    pass


p = Printer('Brother', 10000, 'China', 'Black')
s = shredder('LG', 54000, 'Russia', 'White')
p2 = pamphleteer('Buro', 2000, 'USA', 'Silver')
p.warehouse()
s.warehouse()
p2.warehouse()
