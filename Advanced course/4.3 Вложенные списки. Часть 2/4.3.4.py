# Треугольник Паскаля 2
# На вход программе подается натуральное число 𝑛. Напишите программу, которая выводит первые 𝑛 строк треугольника Паскаля.

# Формат входных данных
# На вход программе подается число 𝑛(𝑛 ≥ 1).

# Формат выходных данных
# Программа должна вывести первые 𝑛 строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

# Тестовые данные 🟢
# Sample Input 1:
# 4
# Sample Output 1:
# 1
# 1 1
# 1 2 1
# 1 3 3 1

# Sample Input 2:
# 5
# Sample Output 2:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

n = int(input())

def triangle(n):
      from math import factorial
      list1 = []
      for i in range(n // 2 + 1):
            list1.append(int(factorial(n) / (factorial(i) * factorial(n - i))))
      if n != 0:
            list1.extend(list1[len(list1) - 2 + (n % 2)::-1])
      return list1

print(*[' '.join(map(str, sublist)) for sublist in [triangle(i) for i in range(n)]], sep='\n')