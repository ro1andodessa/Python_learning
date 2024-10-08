# Заполнение 3
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n × n, заполнив её в соответствии с образцом.

# Формат входных данных
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.

# Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

# Тестовые данные 🟢
# Sample Input 1:
# 5
# Sample Output 1:
# 1  0  0  0  1
# 0  1  0  1  0
# 0  0  1  0  0
# 0  1  0  1  0
# 1  0  0  0  1

# Sample Input 2:
# 4
# Sample Output 2:
# 1  0  0  1
# 0  1  1  0
# 0  1  1  0
# 1  0  0  1

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):    
    matrix[i][i], matrix[i][-i - 1] = 1, 1
    print(' '.join(str(matrix[i][j]).ljust(3) for j in range(n)))

    


# # 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# n = 5
# matrix = []


# for i in range(n):
#     matrix.append([0] * n)
# for i in range(n):    
#     matrix[i][i], matrix[i][-i - 1] = 1, 1
#     print(' '.join(str(matrix[i][j]).ljust(3) for j in range(n)))
    # print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))
# print(matrix, sep='\n')