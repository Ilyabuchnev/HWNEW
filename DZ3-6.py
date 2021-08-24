def my_funk(a):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return a.title() if not set(a).difference(latin_char) else False
earth = input('Введите слова разделенные пробелами ').split()
for e in earth:
    result = my_funk(e)
    if result:
        print(my_funk(e))