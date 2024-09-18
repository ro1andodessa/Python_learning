# a1, b1 = int(input()), int(input())
# a2, b2 = int(input()), int(input())
a1 = 9
b1 = 21
a2 = 7
b2 = 81

if a2 < a1:
    temp_a = a1
    a1 = a2
    a2 = temp_a
    temp_b = b1
    b1 = b2
    b2 = temp_b

if a1 < a2 and b1 == a2 and b1 < b2:
    print(b1)
elif a1 == a2 and b2 < b1:
    print(a1, b2)
elif a1 == a2 and b2 > b1:
    print(a1, b1)
elif a1 < a2 and b1 == b2:
    print(a2, b1)
elif a1 == a2 and b1 == b2:
    print(a2, b2)
elif a1 < a2 < b1 and b1 < b2:
    print(a2, b1)
elif a1 < a2 < b1 and b1 > b2:
    print(a2, b2)
else:
    print('пустое множество')
