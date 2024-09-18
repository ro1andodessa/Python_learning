# Симметричная матрица
# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична относительно главной диагонали, или NO в противном случае.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 0 1 2
# 1 2 3
# 2 3 4
# Sample Output 1:
# YES

# Sample Input 2:
# 3
# 0 1 2
# 1 2 7
# 2 3 4
# Sample Output 2:
# NO

# 🟢🟢🟢🟢🟢   Main     🟢🟢🟢🟢🟢

# n = int(input())
# matrix = []
# is_sim = 'YES'

# matrix = [list(map(int, input().split())) for i in range(n)]

# for row in range(n):
#     for col in range(row):
#         if matrix[col][row] != matrix[row][col]:
#             is_sim = 'NO'
#             break
# print(is_sim)





# 🤔🤔🤔🤔🤔    Test    🤔🤔🤔🤔🤔

n = 3
is_sim = 'YES'
matrix = [[0, 5, 2],
          [5, 2, 3],
          [2, 3, 4]]


for row in range(n):
    for col in range(row):
        if matrix[col][row] != matrix[row][col]:
            is_sim = 'NO'
            break
print(is_sim)