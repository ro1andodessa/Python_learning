# Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.
# Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает суммарное количество товара по данной позиции.

# Формат входных данных
# На вход программе подается число n - количество строк в базе данных о продажах интернет-магазина. Далее следует n строк с записями вида Покупатель Товар Количество, где:
# Покупатель - имя покупателя (строка без пробелов),
# Товар - название товара (строка без пробелов),
# Количество - количество приобретенных единиц товара (натуральное число)

# Формат выходных данных
# Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого покупателя - двоеточие, затем список названий всех приобретенных им товаров в лексиграфическом порядке, после названия каждого товара - количество единиц товара. Информацию о каждом товаре выводится на отдельной строке.

# Sample Input 1:
# 5
# Руслан Пирог 1
# Тимур Карандаш 5
# Руслан Линейка 2
# Тимур Тетрадь 12
# Руслан Хлеб 3

# Sample Output 1:
# Руслан:
# Линейка 2
# Пирог 1
# Хлеб 3
# Тимур:
# Карандаш 5
# Тетрадь 12