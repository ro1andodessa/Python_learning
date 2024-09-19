# Латинский квадрат 🌶️
# Латинским квадратом порядка n называется квадратная матрица размером n × n, каждая строка и каждый столбец которой содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
# '''

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# n = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]

# seq = [i for i in range(1, n + 1)]
# is_lat = 'YES'
# s_row = []

# for i in range(n):
#     s_col = []
#     for j in range(n):
#         s_col.append(matrix[j][i])
#     s_row = matrix[i].copy()
#     s_row.sort()
#     s_col.sort()    
#     if s_row != seq or s_col != seq:
#         is_lat = 'NO'
#         break
        
# print(is_lat)




# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# n = 4
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 3],
#     [8, 9, 6, 2],
#     [4, 8, 5, 1]]
# n = 4
# matrix =[
#     [1, 3, 4, 2],
#     [2, 4, 1, 3],
#     [3, 1, 2, 4],
#     [4, 2, 3, 1]]

n = 4
matrix =[
    [2, 3, 4, 1],
    [3, 4, 1, 2],
    [4, 1, 2, 3],
    [1, 2, 3, 4]]

seq = [i for i in range(1, n + 1)]
is_lat = 'YES'
s_row = []

for i in range(n):
    s_col = []
    for j in range(n):
        s_col.append(matrix[j][i])
    print(s_col)
    s_row = matrix[i].copy()
    s_row.sort()
    s_col.sort()    
    print(f'i = {i}; j = {j}; seq = {seq} ; s_row = {s_row} ; s_col = {s_col}')
    if s_row != seq or s_col != seq:
        is_lat = 'NO'
        break
        
print(is_lat)
    


