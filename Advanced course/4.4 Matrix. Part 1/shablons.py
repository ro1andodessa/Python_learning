# Примечание 2. Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
# Примечание 3. Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)