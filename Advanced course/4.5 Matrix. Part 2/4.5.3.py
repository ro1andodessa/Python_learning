# Обмен столбцов
# Напишите программу, которая меняет местами столбцы в матрице.

# Формат входных данных
# На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

# Формат выходных данных
# Программа должна вывести указанную таблицу с замененными столбцами.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1
# Sample Output 1:
# 12 11 13 14
# 22 21 23 24
# 32 31 33 34

# Sample Input 2:
# 3
# 3
# 11 12 13
# 21 22 23
# 31 32 33
# 2 1
# Sample Output 2:
# 11 13 12 
# 21 23 22 
# 31 33 32 

# 🟢🟢🟢🟢🟢   Main     🟢🟢🟢🟢🟢

# n, m = int(input()), int(input())
# matrix = []

# matrix = [list(map(int, input().split())) for i in range(n)]

# change = list(map(int, input().split()))

# for col in range(n):
#     matrix[col][change[0]], matrix[col][change[1]] = matrix[col][change[1]], matrix[col][change[0]]

# for row in matrix:
#     print(' '.join(map(str, row)))





# 🤔🤔🤔🤔🤔    Test    🤔🤔🤔🤔🤔

n, m = 3, 3
i, j = 0, 2

matrix = [[5, 6, 4],
          [2, 6, 0],
          [4, 1, 6]]


for col in range(n):
    matrix[col][i], matrix[col][j] = matrix[col][j], matrix[col][i]
    
for row in matrix:
    print(' '.join(map(str, row)))