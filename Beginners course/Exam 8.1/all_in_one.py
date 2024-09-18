# Дано натуральное число. Напишите программу, которая вычисляет:
#   количество цифр 3 в нем;
#   сколько раз в нем встречается последняя цифра;
#   количество четных цифр;
#   сумму его цифр, больших пяти;
#   произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
#   сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

n = 17051
counter_of_3 = 0
counter_of_last = 0
counter_of_chet = 0
total_more_than_5 = 0
product_of_more_than_7 = 1
counter_of_0_and_5 = 0
last_digit = n % 10

while n > 0:
    x = n % 10
    if x == 3:
        counter_of_3 += 1
    if x == last_digit:
        counter_of_last += 1
    if x % 2 == 0:
        counter_of_chet += 1
    if x > 5:
        total_more_than_5 += x
    if x > 7:
        product_of_more_than_7 *= x
    if x == 0 or x == 5:
        counter_of_0_and_5 += 1
    n //= 10

print(counter_of_3)
print(counter_of_last)
print(counter_of_chet)
print(total_more_than_5)
print(product_of_more_than_7)
print(counter_of_0_and_5)
    
    