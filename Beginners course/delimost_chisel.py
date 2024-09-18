#n = int(input)
n = 10

for i in range(1, n + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', sep='', end='')
    print()
