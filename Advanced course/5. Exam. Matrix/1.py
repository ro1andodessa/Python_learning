# Каждый n-ый элемент
# На вход программе подается строка текста, содержащая символы и число n. Из данной строки формируется список. Напишите программу, которая разделяет список на вложенные подсписки так, что n последовательных элементов принадлежат разным подспискам.

# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной строке.
# Формат выходных данных
# Программа должна вывести указанный вложенный список.

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

# str_in = input().split()
# n = int(input())
# matrix = [[] for i in range(n)]

# for i in range(len(str_in)):
#     matrix[i % n].append(str_in[i])

# print(matrix)




# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

str_in = '1 2 3 4 5'.split()
n = 3
matrix = [[] for i in range(n)]

for i in range(len(str_in)):
    matrix[i % n].append(str_in[i])

print(matrix)


# print(in_list)

# str_in = input().split(' ')
# n = int(input())
# arr = [[] for _ in range(n)]
# i = 0
# for elem in str_in:
#     arr[i].append(elem)
#     if i == n - 1:
#         i = 0
#     else:
#         i += 1
# print(arr)