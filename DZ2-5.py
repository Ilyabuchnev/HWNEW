list_rating =[8 , 2 , 1]

rating = int(input('Введите целое число: '))
inserted = False
for i, elem in enumerate(list_rating):
    if rating > elem:
        list_rating.insert(i, rating)
        inserted = True
        break
if not inserted:
    list_rating.append(rating)

print(list_rating)

