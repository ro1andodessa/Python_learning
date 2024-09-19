n = total = 63

while n > 9:
    total = 0

    # Считаем сумму цифр числа
    while n > 0:
        total += n % 10
        n //= 10
    n = total
print(total)
