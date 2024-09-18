# Суммы четвертей
# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.

# Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Элементы диагоналей не учитываются.

# Тестовые данные 🟢
# Sample Input 1:
# 4
# 1 2 3 4
# 5 6 7 8
# 3 4 5 6
# 1 2 3 4
# Sample Output 1:
# Верхняя четверть: 5
# Правая четверть: 14
# Нижняя четверть: 5
# Левая четверть: 8

# Sample Input 2:
# 5
# 1 4 3 4 7
# 5 6 7 8 4
# 3 8 5 6 1
# 1 2 9 4 8
# 5 6 1 5 8
# Sample Output 2:
# Верхняя четверть: 18
# Правая четверть: 19
# Нижняя четверть: 21
# Левая четверть: 17

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢
n = int(input())
matrix = []
sum_up, sum_right, sum_down, sum_left = 0, 0, 0, 0

for i in range(n):
    matrix.append([int(num) for num in input().split()])

for i in range(n):
    for j in range(n):
        if (i < j and i < (n - 1 - j)):
            sum_up += matrix[i][j]
        elif (i < j and i > (n - 1 - j)):
            sum_right += matrix[i][j]
        elif (i > j and i > (n - 1 - j)):
            sum_down += matrix[i][j]
        elif (i > j and i < (n - 1 - j)):
            sum_left += matrix[i][j]

print('Верхняя четверть:', sum_up)
print('Правая четверть:', sum_right)
print('Нижняя четверть:', sum_down)
print('Левая четверть:', sum_left)


# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔
n = 4
matrix = [[14, 13, 12, 10],
          [15, 16, 11, 17],
          [17, 18, 19, 12],
          [11, 14, 13, 18]]
sum_up, sum_right, sum_down, sum_left = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if (i < j and i < (n - 1 - j)):
            sum_up += matrix[i][j]
        elif (i < j and i > (n - 1 - j)):
            sum_right += matrix[i][j]
        elif (i > j and i > (n - 1 - j)):
            sum_down += matrix[i][j]
        elif (i > j and i < (n - 1 - j)):
            sum_left += matrix[i][j]

print('Верхняя четверть:', sum_up)
print('Правая четверть:', sum_right)
print('Нижняя четверть:', sum_down)
print('Левая четверть:', sum_left)
