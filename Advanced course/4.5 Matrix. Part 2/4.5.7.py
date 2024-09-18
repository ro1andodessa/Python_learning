# Поворот матрицы
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
# 7 4 1 
# 8 5 2 
# 9 6 3 

# Sample Input 2:
# 4
# 1 9 4 2
# 3 8 1 5
# 6 7 4 6
# 1 9 7 8
# Sample Output 2:
# 1 6 3 1
# 9 7 8 9
# 7 4 1 4
# 8 6 5 2

# 🟢🟢🟢🟢🟢   Main     🟢🟢🟢🟢🟢

# n = int(input())
# matrix = []
# rotate_matrix = []

# matrix = [list(map(int, input().split())) for i in range(n)]

# for i in range(n):
#     rotate_matrix.append([matrix[-j - 1][i] for j in range(n)])

# for row in rotate_matrix:
#     print(' '.join(map(str, row)))





# 🤔🤔🤔🤔🤔    Test    🤔🤔🤔🤔🤔

n = 3
matrix = [[1, 5, 6],
          [5, 5, 3],
          [4, 3, 3]]

rotate_matrix = []

# matrix = [[1, 5, 6, 7],
#           [5, 5, 3, 0],
#           [4, 3, 3, 1],
#           [2, 8, 9, 3]]

for i in range(n):
    rotate_matrix.append([matrix[-j - 1][i] for j in range(n)])

for row in rotate_matrix:
    print(' '.join(map(str, row)))

print(*rotate_matrix, sep='\n')