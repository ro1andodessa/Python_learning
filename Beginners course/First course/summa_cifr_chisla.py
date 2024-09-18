# объявление функции
def print_digit_sum(num):
    total = 0
    # while num > 0:
    #     total += num % 10
    #     num //= 10
    #num = str(num)
    #print(type(num))
    num = 223
    print(sum(int(i) for i in str(num)))
    #print(total)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)