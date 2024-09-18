from math import factorial

n = 3
total = 0

for i in range(1, n + 1):
    total += factorial(i)

print(total)

# Факториал числа n
n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)
