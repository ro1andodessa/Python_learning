# Змеиный регистр 🐍
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

# Приведённый ниже код:
    # print(convert_to_python_case('ThisIsCamelCased'))
    # print(convert_to_python_case('IsPrimeNumber'))

# должен выводить:
    # this_is_camel_cased
    # is_prime_number

# объявление функции
def convert_to_python_case(text):
    # s = ''
    # for i in text:
    #     if i.isupper():
    #         s += '_' + i.lower()
    #     else:
    #         s += i
    
        
    return ''.join('_' + i.lower() if i.isupper() else i for i in text)[1:]

# считываем данные
txt = 'ConvertToInt32'

# вызываем функцию
print(convert_to_python_case(txt))