# Умножение матриц 🌶️
# Напишите программу, которая перемножает две матрицы.

# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем элементы второй матрицы.

# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

# Тестовые данные 🟢
# Sample Input 1:
# 2 2
# 1 2
# 3 2

# 2 2
# 3 2
# 1 1
# Sample Output 1:
# 5 4
# 11 8

# Sample Input 2:
# 3 2
# 2 5
# 6 7
# 1 8

# 2 3
# 1 2 1
# 0 1 0

# Sample Output 2:
# 2 9 2
# 6 19 6
# 1 10 1

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# n, m = [int(_) for _ in input().split()]
# matrix1, matrix2 = [], []
# matrix1 = [list(map(int, input().split())) for i in range(n)]
# input()
# matrix2 = [list(map(int, input().split())) for i in range(n)]

# print(matrix1, matrix2, sep='\n')
# for i in range(n):
#     for j in range(m):
#         matrix1[i][j] += matrix2[i][j]

# for row in matrix1:
#     print(*row)

    


# # 🤔🤔🤔🤔 Test 🤔🤔🤔🤔
# 5 4
# 11 8

n, m = [int(_) for _ in '2 2'.split()]
matrix1, matrix2 = [], []
matrix1 = [[1, 2],
           [3, 2]]
matrix2 = [[2, 2],
           [3, 2]]
res_mat = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        res_mat[i][i % m] += matrix1[i][j] * matrix2[j][i]
        

for row in res_mat:
    print(*row)