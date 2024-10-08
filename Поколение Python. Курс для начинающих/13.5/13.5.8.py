# BEEGEEK 🐝
# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка, или False в противном случае.

#  Примечание. Следующий программный код:

# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))
# 1221:101:22:22
# должен выводить:

# True
# False
# False
# False

# объявление функции
def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True
    
def is_valid_password(password):
    #elements = password.split(':')
    return True if password.split(':')[0] == password.split(':')[0][::-1] and is_prime(int(password.split(':')[1])) and int(password.split(':')[2]) % 2 ==0 and len(password.split(':')) == 3 else False

# считываем данные
psw = '1221:101:22:22'

# вызываем функцию
print(is_valid_password(psw))