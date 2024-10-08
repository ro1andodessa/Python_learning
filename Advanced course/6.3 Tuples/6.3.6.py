# Конкурсный отбор
# Напишите программу, которая выводит список хорошистов и отличников в классе.

# Формат входных данных
# На вход программе подается натуральное число n, далее следует n строк с фамилией школьника и его оценкой на каждой из них.

# Формат выходных данных
# Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке. Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

# Примечание 1. Оценка ученика – это натуральное число от 1 до 5.

# Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист (обладатель оценки 4) или отличник (получивший 5).

# Тестовые данные 🟢
# Sample Input 1:
# 3
# Гуев 3
# Чаниев 5
# Барсуков 2
# Sample Output 1:
# Гуев 3
# Чаниев 5
# Барсуков 2

# Чаниев 5

# Sample Input 2:
# 5
# Круглов 4
# Кузнецов 5
# Федин 4
# Тарасов 2
# Словецкий 3

# Sample Output 2:
# Круглов 4
# Кузнецов 5
# Федин 4
# Тарасов 2
# Словецкий 3

n = int(input())
student = tuple(tuple(input().split()) for i in range(n))
for i in student:
    print(*i)
print()
for i in student:
    if int(i[1]) >= 4:
        print(*i)