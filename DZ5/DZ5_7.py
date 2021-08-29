import json
with open('dz5z7.txt', encoding='utf-8') as f, open('7j.txt', 'w', encoding='utf-8') as f1 :
    profit = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in f}
    res = [profit, {'Средний доход компаний': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                               len([int(i) for i in profit.values() if int(i) > 0]))}]


    json.dump(res, f1)
