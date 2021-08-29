
with open('dz5z3.txt','r', encoding='utf-8') as f:
   dict = {i.split()[0]: int(i.split()[1]) for i in f}
   print(f'Сотрудники с зарплатой менее 20 т.р.= {[i[0] for i in dict.items() if i[1] < 20000]}')
   print(f'Средняя величина дохода сотр.= {sum(dict.values()) / len(dict)}')

