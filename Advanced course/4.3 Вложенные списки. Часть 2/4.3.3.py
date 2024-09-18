# Треугольник Паскаля 1 🌶️
# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....
# На вход программе подается число 𝑛. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).

# Формат входных данных
# На вход программе подается число 𝑛(𝑛 ≥ 0).

# Формат выходных данных
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.

# Примечание 1. Решение удобно оформить в виде функции pascal(), которая принимает номер строки и возвращает соответствующую строку треугольника Паскаля.

# Sample Input 2:
# 1
# Sample Output 2:
# [1, 1]

# Sample Input 3:
# 2
# Sample Output 3:
# [1, 2, 1]

# Sample Input 4:
# 3
# Sample Output 4:
# [1, 3, 3, 1]

# V1
# from math import factorial

# n = int(input())
# list1 = []

# for i in range(n // 2 + 1):
#     list1.append(int(factorial(n) / (factorial(i) * factorial(n - i))))
# list1.extend(reversed(list1[:len(list1) - (not n % 2)]))

# print(list1)

# V2


n = int(input())

def triangle(n):
      from math import factorial
      list1 = []
      for i in range(n // 2 + 1):
            list1.append(int(factorial(n) / (factorial(i) * factorial(n - i))))
      if n != 0:
            list1.extend(list1[len(list1) - 2 + (n % 2)::-1])
      return list1

print(triangle(n))
