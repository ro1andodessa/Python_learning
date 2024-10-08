# Онлайн-школа BEEGEEK 5 🌶️
# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников перемешались.
# Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

# Формат входных данных.
# На вход программе в первых двух строках подаются числа m и n - количества учеников, изучающих математику и информатику соответственно. Далее идут m + n строк - фамилии учеников, изучающих математику и информатику в произвольном порядке.

# Формат выходных данных.
# Программа должна вывести количество учеников, которые изучают только один предмет. Если таких учеников нет, то необходимо вывести NO. 

m, n = int(input()), int(input())
std_list = [input() for i in range(m + n)]
std_set = set(std_list)
res = len(std_set) - (len(std_list) - len(std_set))
print(res if res > 0 else 'NO')