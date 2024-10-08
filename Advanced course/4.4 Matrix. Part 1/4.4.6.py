# Максимальный в области 2 🌶️
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# 1 0 1
# 1 1 1
# 1 0 1 

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

# Примечание. Элементы диагоналей также учитываются.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 1 4 5
# 6 7 8
# 1 1 6
# Sample Output 1:
# 8

# Sample Input 2:
# 4
# 0 1 4 6
# 0 0 2 5
# 0 0 0 7
# 0 0 0 0
# Sample Output 2:
# 7

#🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢
n = int(input())
matrix = []
maximum = 0

for i in range(n):
    matrix.append([int(num) for num in input().split()])

for i in range(n):
    for j in range(n):
        if (i >= j and i <= (n - 1 - j)) or (i <= j and i >= (n - 1 - j)):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)


# Test
n = 3
matrix = [[14, 13, 12],
          [15, 16, 11],
          [17, 18, 19]]
maximum = 0

for i in range(n):
    for j in range(n):
        if (i >= j and i <= (n - 1 - j)) or (i <= j and i >= (n - 1 - j)):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)