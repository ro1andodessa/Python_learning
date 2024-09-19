# Максимальный в области 2
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
# Примечание. Элементы побочной диагонали также учитываются.
# '''

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
max = matrix[-1][-1]

for i in range(-1, -n - 1, -1):
    for j in range(-1, -n - 2 - i, -1):
        if matrix[i][j] > max:
            max = matrix[i][j]

print(max)




# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# n = int(input())
matrix = []
# for i in range(n):
# matrix.append([input().split() for i in range(n)])
# max = matrix[-1][-1]

# n = 4
# matrix = [[14, 13, 12, 25],
#           [15, 16, 24, 21],
#           [17, 23, 19, 12],
#           [22, 14, 13, 18]]
# max = matrix[-1][-1]

# for i in range(-1, -n - 1, -1):
#     for j in range(-1, -n - 2 - i, -1):
#         if matrix[i][j] > max:
#             max = matrix[i][j]



# print(max)
# print(*matrix)
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# max_matrix = -999
# for r in range(n):
#     for c in range(n):
#         if (c == n - r - 1) or (r < c and r > n - 1 - c) or (r > c and r > n - 1 - c) or (r == c and r >= n / 2):
#             if matrix[r][c] > max_matrix:
#                 max_matrix = matrix[r][c]

# print(max_matrix)