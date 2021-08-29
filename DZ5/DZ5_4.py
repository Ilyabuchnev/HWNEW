w = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text2.txt', 'w',encoding='utf-8') as f1, open('dz5z4-1.txt','r') as f:
    f1.write(str([i.replace(i.split()[0],w.get(i.split()[0])) for i in f]))
