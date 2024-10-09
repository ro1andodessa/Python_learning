# Самое редкое слово 🌶️
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

# Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.

# Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.

# Тестовые данные 🟢
# Sample Input 1:
# home sweet home
# Sample Output 1:
# sweet

# Sample Input 2:
# home sweet home sweet.
# Sample Output 2:
# home
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'


result = {}
s = input().lower()

for i in s.split():
    result[i.strip('.,!?:;-,')] = result.get(i.strip('.,!?:;-,'), 0) + 1
min_word = [key for key, value in result.items() if result[key] == min(result.values())]

print(min(min_word))