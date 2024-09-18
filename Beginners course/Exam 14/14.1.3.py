# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n, k и возвращает значение биномиального коэффициента, равного n! / k! * (n-k)!

def compute_binom(n, k):
    from math import factorial
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

print(compute_binom(int(input()), int(input())))