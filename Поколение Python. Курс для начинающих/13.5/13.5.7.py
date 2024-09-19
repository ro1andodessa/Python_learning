# Палиндром 🌶️
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.

# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

# Примечание 3. Следующий программный код:

# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))
# должен выводить:

# True
# True
# False

# объявление функции
def is_palindrome(text):
    # Creating a string that contains all the letters from "text" and converting them to lowercase
    # s = ''.join(i.lower() for i in text if i.isalpha())

    # Checking if "s" equal to it's reverse
    # if s == s[::-1]:
    #     return True
    # else:
    #     return False

    return True if ''.join(i.lower() for i in text if i.isalpha()) == ''.join(i.lower() for i in text if i.isalpha())[::-1] else False
    

# считываем данные
txt = 'А роза упала на лапу Азора.'

# вызываем функцию
print(is_palindrome(txt))