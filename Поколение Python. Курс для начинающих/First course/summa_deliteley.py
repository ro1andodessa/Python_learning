a, b = 1, 10
sum, sum_max = 0, 0
# for i in range(a, b + 1):

# Находит все делители числа и их сумму
for j in range(1, b + 1):
    if b % j == 0:
        sum += j
        # print(j)
print(sum)
