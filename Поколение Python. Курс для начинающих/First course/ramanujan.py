count = 0  # Счетчик найденных чисел Рамануджана
limit = 100  # Начальный предел для кубов
ramanujan_numbers_found = 0  # Число найденных чисел Рамануджана

while ramanujan_numbers_found < 5:
    for a in range(1, limit):
        for b in range(a + 1, limit):
            for c in range(a + 1, limit):
                for d in range(c + 1, limit):
                    if a**3 + b**3 == c**3 + d**3:
                        ramanujan_number = a**3 + b**3
                        ramanujan_numbers_found += 1
                        print(
                            f"{ramanujan_numbers_found}: {ramanujan_number} = {a}^3 + {b}^3 = {c}^3 + {d}^3"
                        )
                        if ramanujan_numbers_found == 5:
                            break
                if ramanujan_numbers_found == 5:
                    break
            if ramanujan_numbers_found == 5:
                break
        if ramanujan_numbers_found == 5:
            break
    limit *= 2
