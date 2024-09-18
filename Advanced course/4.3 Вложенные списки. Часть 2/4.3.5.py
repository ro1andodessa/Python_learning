# Упаковка дубликатов 🌶️
# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

# Формат выходных данных
# Программа должна вывести указанный вложенный список.

# Тестовые данные 🟢
# Sample Input 1:
# a b c d
# Sample Output 1:
# [['a'], ['b'], ['c'], ['d']]

# Sample Input 2:
# w w w o r l d g g g g r e a t t e c c h e m g g p w w
# Sample Output 2:
# [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]

# list1 = [[i] for i in input().split()]
# # for i in range(len(list1) - 1):
# #     if list1[i] == list1[i + 1]:
# #         list1[i].append()
# print(list1)

# V1
# s ='abbbccchhhhykkkll'
s = ''.join(input().split())
a = 0
list1 = [list(s[0])]

for i in range(1, len(s)):
    if s[i] in list1[a]:
        list1[a].append(s[i])
    else:
        list1.append([s[i]])
        a += 1

print(list1)

# V2 чужое решение

s = input().split()
seq = [[s.pop(0)]]

for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])

print(seq)


