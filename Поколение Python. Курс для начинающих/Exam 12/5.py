# Самый длинный

# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# s = input().split()
# d = [len(s[i]) for i in range(len(s))]
print(max([len(i) for i in input().split()]))
