# Заполнение 5 🌶️
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n × m, заполнив её в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение. 😇

# Тестовые данные 🟢
# Sample Input 1:
# 5 5
# Sample Output 1:
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4

# Sample Input 2:
# 6 6
# Sample Output 2:
# 1 2 3 4 5 6
# 2 3 4 5 6 1
# 3 4 5 6 1 2
# 4 5 6 1 2 3
# 5 6 1 2 3 4
# 6 1 2 3 4 5

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# n, m = [int(_) for _ in input().split()]
# matrix = []
# m_list = [i for i in range(1, m + 1)]

# print(m_list)
# for i in range(n):
#     matrix.append([m_list[i % m + j - m] for j in range(m)])
#     print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))

    


# # 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

n, m = 7, 3
matrix = []
m_list = [i for i in range(1, m + 1)]

print(m_list)
for i in range(n):
    matrix.append([m_list[i % m + j - m] for j in range(m)])
    print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))
# for i in range(n):    
#     print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))