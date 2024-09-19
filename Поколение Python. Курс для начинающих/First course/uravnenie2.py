def find_euler_solution():
    limit = 150  # Можно увеличить предел для более точного поиска
    for a in range(1, limit):
        a5 = a**5
        for b in range(a, limit):
            b5 = b**5
            for c in range(b, limit):
                c5 = c**5
                for d in range(c, limit):
                    d5 = d**5
                    e5 = a5 + b5 + c5 + d5
                    e = round(e5 ** (1 / 5))
                    if e**5 == e5:
                        print(f"Найдено решение: a={a}, b={b}, c={c}, d={d}, e={e}")
                        print(f"Сумма a + b + c + d + e = {a + b + c + d + e}")
                        return a, b, c, d, e


# Запуск функции для поиска решения
find_euler_solution()
