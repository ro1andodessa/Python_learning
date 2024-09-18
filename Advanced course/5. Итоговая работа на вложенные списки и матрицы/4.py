# Снежинка
# На вход программе подается нечетное натуральное число n. Напишите программу, которая создает матрицу размером  n × n заполнив её символами . . Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.
# Формат входных данных
# На вход программе подается нечетное натуральное число n, где n ≥ 3 — количество строк и столбцов в матрице.
# '''

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

n = int(input())
matrix = [['.'] * n for i in range(n)]

for i in range(n):
    matrix[i][i] = '*'
    matrix[-i - 1][i] = '*'
    matrix[n // 2][i] = matrix[i][n // 2] = '*'

for row in matrix:
    print(*row)




# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# n = int(input())
# matrix = []
# n = 4
# matrix = [[14, 13, 12, 25],
#           [15, 16, 24, 21],
#           [17, 23, 19, 12],
#           [22, 14, 13, 18]]

# for i in range(n):
#     for j in range(i, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# print(*matrix, sep='\n')



# import math

# n = int(input())

# matrix = [['.'] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if (i == j) or (j == n - i - 1) or (i == math.floor(n / 2) or (j == math.floor(n / 2))):
#             matrix[i][j] = '*'
#         print(matrix[i][j], end=' ')
#     print()