# Заполнение диагоналями 🌶️
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n × m, заполнив её "диагоналями" в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

# Тестовые данные 🟢
# Sample Input 1:
# 3 5
# Sample Output 1:
# 1  2  4  7  10
# 3  5  8  11 13
# 6  9  12 14 15

# Sample Input 2:
# 3 4
# Sample Output 2:
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for i in range(n)]
# print(*matrix)

# for i in range(n):
#     matrix.append([i * m + j  for j in range(1, m + 1)])
    
#     print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))


# # 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# 1 4 7 10
# 2 5 8 11
# 3 6 9 12

n, m = [int(i) for i in '3 5'.split()]
matrix = [[0] * m for i in range(n)]

print(n, m)
k = 0

while k <= n * m:

    for i in range(k):
        for j in range(m - k):
            if i + j == k:
                matrix[i][j] = k
                k += 1

    # print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))
print(*matrix, sep='\n')