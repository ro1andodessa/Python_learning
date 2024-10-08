# Обмен диагоналей
# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
# 7 2 9 
# 4 5 6 
# 1 8 3 

# Sample Input 2:
# 2
# 1 2
# 4 5
# Sample Output 2:
# 4 5
# 1 2

# 🟢🟢🟢🟢🟢   Main     🟢🟢🟢🟢🟢

# n = int(input())
# matrix = []

# matrix = [list(map(int, input().split())) for i in range(n)]

# for i in range(n):
#     matrix[i][i], matrix[-i - 1][i] = matrix[-i - 1][i], matrix[i][i]

# for row in matrix:
#     print(' '.join(map(str, row)))





# 🤔🤔🤔🤔🤔    Test    🤔🤔🤔🤔🤔

n = 3
matrix = [[1, 5, 6],
          [5, 5, 3],
          [4, 3, 3]]

for i in range(n):
    matrix[i][i], matrix[-i - 1][i] = matrix[-i - 1][i], matrix[i][i]

for row in matrix:
    print(' '.join(map(str, row)))