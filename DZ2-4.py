string = input('Введите слова через пробелы ').split()
for i, string in enumerate(string, 1):
    print(f'{i}, {string[:10]}')