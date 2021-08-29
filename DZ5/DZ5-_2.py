with open('dz5z2.txt','r', encoding='utf-8') as file2:
   a = file2.read().split('\n')
   num_str = len(a) - 1
   w = 0
   for i in file2:
      ws = i.split()
      w += len(ws)
   print(num_str)
   print(w)

# l = 0
# w = 0
# f = open('dz5z2.txt','r')
# for i in f:
#    l += 1
#    ws = i.split()
#    w += len(ws)
# f.close()
# print(l)
# print(w)
