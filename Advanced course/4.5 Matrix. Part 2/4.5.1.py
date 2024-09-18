# Таблица умножения
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице. Создайте матрицу mult размером n × m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

# Формат входных данных
# На вход программе на разных строках подаются два числа n и m — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа (для этого используйте строковый метод ljust()).

# Тестовые данные 🟢
# Sample Input 1:
# 4
# 6
# Sample Output 1:
# 0  0  0  0  0  0
# 0  1  2  3  4  5
# 0  2  4  6  8  10
# 0  3  6  9  12 15

# Sample Input 2:
# 3
# 5
# Sample Output 2:
# 0  0  0  0  0
# 0  1  2  3  4
# 0  2  4  6  8

# 🟢🟢🟢🟢🟢   Main     🟢🟢🟢🟢🟢

n, m = int(input()), int(input())
mult = []

for i in range(n):
    mult.append([i * j for j in range(m)])
    print(' '.join(str(mult[i][j]).ljust(3) for j in range(m)))

# print(mult)





# 🤔🤔🤔🤔🤔    Test    🤔🤔🤔🤔🤔

n, m = 5, 6
mult = []

for i in range(n):
    mult.append([i * j for j in range(m)])
    print(' '.join(str(mult[i][j]).ljust(3) for j in range(m)))

# print(*(' '.join(str(mult[i])) for i in range(n)), sep='\n')
# for i in range(n):
#     print(' '.join(str(mult[i][j]).ljust(3) for j in range(m)))