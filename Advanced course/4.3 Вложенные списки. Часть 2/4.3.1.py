# Список по образцу 1
# На вход программе подается число 𝑛. Напишите программу, которая создает и выводит построчно список, состоящий из 𝑛 списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

# Формат входных данных
# На вход программе подается натуральное число 𝑛.

# Формат выходных данных
# Программа должна вывести построчно указанный список.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# Sample Output 1:
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]

n = int(input())

list1 = [[i for i in range(1, n + 1)]for i in range(n)]
print(*list1, sep='\n')
