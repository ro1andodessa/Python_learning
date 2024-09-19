# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language - язык и number - номер месяца и возвращает название месяца на русском или английском языке.

def get_month(language, number):
    month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    return month[number - 1] if language == 'ru' else month[number + 11]

print(get_month('en', 6))