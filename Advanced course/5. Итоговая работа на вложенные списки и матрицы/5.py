# Симметричная матрица
# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
# '''

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]

# is_sim = 'YES'

# for i in range(n):
#     for j in range(n - i):
#         if matrix[i][j] != matrix[-j - 1][-i - 1]:
#             is_sim = 'NO'
#             break




# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# n = 4
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 3],
#     [8, 9, 6, 2],
#     [4, 8, 5, 1]]
n = 5
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]
is_sim = 'YES'

for i in range(n):
    for j in range(n - i):
        if matrix[i][j] != matrix[-j - 1][-i - 1]:
            is_sim = 'NO'
            break

print(is_sim)











# n = int(input())

# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)

# trans_matrix = [[matrix[i][j] for i in range(n - 1, -1, -1)] for j in range(n - 1, -1, -1)]

# if matrix == trans_matrix:
#     print("YES")
# else:
#     print("NO")