# Телефонная книга 📒
# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

# У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру находить все номера определённого друга.

# Формат входных данных
# В первой строке задано одно целое число n — количество номеров телефонов, информацию о которых Тимур сохранил в телефонной книге. В следующих n строках заданы телефоны и имена их владельцев через пробел. В следующей строке записано целое число m — количество поисковых запросов от Тимура. В следующих m строках записаны сами запросы, по одному на строке. Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти.

# Формат выходных данных
# Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем (независимо от регистра имени). Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «абонент не найден» (без кавычек).

# Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во входных данных.

# Примечание 2. Количество строк в ответе должно быть равно числу  m.

# Примечание 3. Телефон — это несколько цифр, записанных подряд, а имя может состоять из букв русского или английского алфавита. Записи не повторяются.

# Тестовые данные 🟢

# Sample Input:
# 3
# 79184219577 Женя
# 79194249271 Руслан
# 79281234567 Женя
# 3
# Руслан
# женя
# Рустам

# Sample Output:
# 79194249271
# 79184219577 79281234567
# абонент не найден

dict1 = {}

for i in range(int(input())):
    value, key = input().lower().split()
    if key not in dict1.keys():
        dict1[key] = value
    else:
        dict1[key] = dict1[key] + ' ' + value

for i in range(int(input())):
    print(dict1.get(input().lower(), 'абонент не найден'))




dct = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    dct.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))