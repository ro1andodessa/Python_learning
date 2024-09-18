# Сложение матриц
# Напишите программу для вычисления суммы двух матриц.

# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

# Тестовые данные 🟢
# Sample Input 1:
# 2 4
# 1 2 3 4
# 5 6 7 1

# 3 2 1 2
# 1 3 1 3
# Sample Output 1:
# 4 4 4 6
# 6 9 8 4

# Sample Input 2:
# 3 3
# 9 6 3
# 3 1 1
# 4 7 5

# 0 3 2
# 1 7 8
# 4 2 3
# Sample Output 2:
# 9 9 5
# 4 8 9
# 8 9 8

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# n, m = [int(_) for _ in input().split()]
# matrix1, matrix2 = [], []
# matrix1 = [list(map(int, input().split())) for i in range(n)]
# y = input()
# matrix2 = [list(map(int, input().split())) for i in range(n)]

# print(matrix1, matrix2, sep='\n')
# for i in range(n):
#     for j in range(m):
#         matrix1[i][j] += matrix2[i][j]

# for row in matrix1:
#     print(*row)

    


# # 🤔🤔🤔🤔 Test 🤔🤔🤔🤔


n, m = [int(_) for _ in '2 4'.split()]
matrix1, matrix2 = [], []
matrix1 = [[1, 1, 1, 1],
           [2, 2, 2, 2]]
matrix2 = [[2, 2, 2, 2],
           [3, 3, 3, 3]]

for i in range(n):
    for j in range(m):
        matrix1[i][j] += matrix2[i][j]

for row in matrix1:
    print(*row)