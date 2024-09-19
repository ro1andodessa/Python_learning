a, b = 49, 56
sum, sum_max, num = 0, 0, 0

for i in range(a, b + 1):   # Цикл перебора чисел из диапазона a:b
    
    sum = 0
    for j in range(1, i + 1):   # Находит все делители числа и их сумму
        if i % j == 0:
            sum += j
            #print(j)
    if sum >= sum_max:   # Проверка максимальная ли сумма. Если нова > старой, то перезаписываем новым значением
        sum_max = sum
        num = i

print(num, sum_max)