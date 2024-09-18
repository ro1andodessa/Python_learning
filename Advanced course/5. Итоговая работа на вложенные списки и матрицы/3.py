# Транспонирование матрицы
# Напишите программу, которая транспонирует квадратную матрицу.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

# Формат выходных данных
# Программа должна вывести транспонированную матрицу.
# Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.
# Примечание 2. Задачу можно решить без использования вспомогательного списка.
# '''

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# n = int(input())
# matrix = []
# matrix.append([input().split() for i in range(n)])

# for i in range(-1, -n - 1, -1):
#     for j in range(-1, -n - 2 - i, -1):
#         if matrix[i][j] > max:
#             max = matrix[i][j]

# print(max)




# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# n = int(input())
matrix = []
n = 4
matrix = [[14, 13, 12, 25],
          [15, 16, 24, 21],
          [17, 23, 19, 12],
          [22, 14, 13, 18]]

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]




print(*matrix, sep='\n')





# n = int(input())

# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# trans_matrix = [[matrix[i][j] for i in range(n)] for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         print(trans_matrix[i][j], end=' ')
#     print()