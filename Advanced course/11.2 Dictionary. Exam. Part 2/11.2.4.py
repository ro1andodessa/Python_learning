# Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного знака и идет до конца адреса. Например:
# https://beegeek.ru?name=timur     # строка запроса: name=timur
# Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
# https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green 
# Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров.

# Примечание 1. В итоговой строке параметры должны быть отсортированы в лексикографическом порядке ключей словаря.

# Примечание 2. Следующий программный код:
# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
# должен выводить:
# age=28&name=timur
# game=2&sport=hockey&time=17
# Примечание 3. Вызывать функцию build_query_string() не нужно, требуется только реализовать. 

# dict1 = {'sport': 'hockey', 'game': 2, 'time': 17}

def build_query_string(d):
    # s = '&'.join(str(k) + '=' + str(v) for k, v in sorted(d.items()))
    return '&'.join(str(k) + '=' + str(v) for k, v in sorted(d.items()))

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
