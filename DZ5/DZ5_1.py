with open('text1.txt', 'w') as file1:
    while True:
        string_text = input("Введите строку: ")
        if not string_text:
            break
        file1.write(f'{string_text}\n')



