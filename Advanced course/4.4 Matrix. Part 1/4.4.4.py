# Больше среднего
# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

# Формат выходных данных
# Программа должна вывести n чисел — для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной строки.

# Тестовые данные 🟢
# Sample Input 1:
# 4
# 1 2 3 4
# 5 6 3 15
# 0 2 3 1
# 5 2 8 5
# Sample Output 1:
# 2
# 1
# 2
# 1

# Sample Input 2:
# 2
# 5 6
# 99 5
# Sample Output 2:
# 1
# 1

n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(num) for num in input().split()]) 

for i in range(n):
    counter = 0
    for j in range(n):
        if matrix[i][j] > sum(matrix[i]) / n:
            counter +=1
    print(counter)
