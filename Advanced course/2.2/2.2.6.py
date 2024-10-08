# Произведение чисел
# Напишите программу для определения, является ли число произведением двух чисел из данного набора. Программа должна выводить результат в виде ответа «ДА» или «НЕТ».

# Формат входных данных
# В первой строке подаётся натуральное число 𝑛 (0 < 𝑛 < 1000) – количество чисел в наборе. В последующих n строках вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

# Формат выходных данных
# Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

# Примечание 1. Само на себя число из набора умножиться не может. Другими словами, два множителя должны иметь разные индексы в наборе.

# Примечание 2. Для решения задачи используйте вложенные циклы.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 33
# 17
# 35
# 999
# Sample Output 1:
# НЕТ

# Sample Input 2:
# 4
# 89
# 4
# 77
# 4
# 16
# Sample Output 2:
# ДА

# n = int(input())
numbers = [int(input()) for _ in range(int(input()) + 1)]

result = 'NO'
for i in range(len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
        if numbers[i] * numbers[j] == numbers[-1]:
            result = 'YES'
            break
print(result)
