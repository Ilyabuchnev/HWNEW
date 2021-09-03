dict = {}
with open('dz5z6.txt', encoding='utf-8') as f:
    for i in f:
        obj, nums = i.split(':')
        elem = [i for i in nums if i == ' ' or (i >= '0' and i <= '9')]
        obj_s = sum(map(int, ''.join(elem).split()))
        dict[obj] = obj_s
print(f'{dict}')
