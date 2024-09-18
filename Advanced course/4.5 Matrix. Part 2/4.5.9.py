# Магический квадрат 🌶️
# Магическим квадратом порядка n называется квадратная таблица размера n × n, составленная из всех чисел 1, 2, 3, …, n**2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести YES, если матрица является магическим квадратом, или NO в противном случае.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 8 1 6
# 3 5 7
# 4 9 2
# Sample Output 1:
# YES

# Sample Input 2:
# 3
# 8 2 6
# 3 5 7
# 4 9 1
# Sample Output 2:
# NO

# 🟢🟢🟢🟢🟢   Main     🟢🟢🟢🟢🟢

n = int(input())
matrix = []

matrix = [list(map(int, input().split())) for i in range(n)]

flag = 'YES'
etalon = sum(matrix[0])
sum_main_diag, sum_sec_diag = 0, 0
seq = ''.join(str(i) for i in range(1, n**2 + 1))
seq_matrix = []

for i in range(n):
    sum_col, sum_row = 0, 0
    for j in range(n):
        seq_matrix.append(matrix[i][j])
        sum_col += matrix[j][i]
        sum_row += matrix[i][j]
    
    if sum_col != etalon or sum_row != etalon:
        flag = 'NO'
        break
    
    sum_main_diag += matrix[i][i]
    sum_sec_diag += matrix[-i - 1][-i - 1]
seq_matrix.sort()

if sum_main_diag != etalon or sum_sec_diag != etalon or seq != ''.join(str(seq_matrix[i]) for i in range(len(seq_matrix))):
    flag = 'NO'

print(flag)





# 🤔🤔🤔🤔🤔    Test    🤔🤔🤔🤔🤔

n = 6
matrix = [[27, 29, 2, 4, 13, 36],
          [9, 11, 20, 22, 31, 18],
          [32, 25, 7, 3, 21, 23],
          [14, 16, 34, 30, 12, 5],
          [28, 6, 15, 17, 26, 19],
          [1, 24, 33, 35, 10, 8]]

# n = 3
# matrix = [[8, 1, 6],
#           [3, 5, 7],
#           [4, 9, 2]]

# n = 3
# matrix = [[5, 5, 5],
#           [5, 5, 5],
#           [5, 5, 5]]

flag = 'YES'
etalon = sum(matrix[0])
sum_main_diag, sum_sec_diag = 0, 0
seq = ''.join(str(i) for i in range(1, n**2 + 1))
seq_matrix = []

for i in range(n):
    sum_col, sum_row = 0, 0
    for j in range(n):
        seq_matrix.append(matrix[i][j])
        sum_col += matrix[j][i]
        sum_row += matrix[i][j]
    
    if sum_col != etalon or sum_row != etalon:
        flag = 'NO'
        break
    
    sum_main_diag += matrix[i][i]
    sum_sec_diag += matrix[-i - 1][-i - 1]
seq_matrix.sort()

if sum_main_diag != etalon or sum_sec_diag != etalon or seq != ''.join(str(seq_matrix[i]) for i in range(len(seq_matrix))):
    flag = 'NO'

print(flag)
    

