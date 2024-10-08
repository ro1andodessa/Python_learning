# Диагонали параллельные главной
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:
# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, число 1;
# на следующих двух диагоналях число 2, и т.д.

# Формат входных данных
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести матрицу в соответствии с условием задачи.
# '''

n = int(input())
matrix = [[0] * n for _  in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)

for row in matrix:
    print(*row)





# n = int(input())

# matrix = [[0 for j in range(n)] for i in range(n)]

# for i in range(n):
#     for j in range(n):
#         matrix[i][j] = abs(i - j)
#         print(matrix[i][j], end=' ')
#     print()