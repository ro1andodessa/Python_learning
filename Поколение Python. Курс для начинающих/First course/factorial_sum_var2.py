from math import factorial

n = 10
total = 0
total_product = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        total_product *= j
        # print(total_product)
    total += total_product
    total_product = 1

print(total)


# Факториал числа n
n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)
