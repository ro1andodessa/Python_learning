s = 'abc, ababc: cba'
dict1 = {}
for i in s.split():
    for j in i.strip('.,!?:;-'):
        dict1[j] = dict1.get(j, 0) +1

print(dict1)