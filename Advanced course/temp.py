<<<<<<< HEAD
s = '1 1 2 2 5 5 5 5 6 7 8'
numbers = [int(i) for i in s.split()]
numbers_set = set()
print(numbers)
for i in numbers:
    if i in numbers_set:
        print('YES')
    else:
        print('NO')
    numbers_set.add(i)

print(numbers_set)
=======
print(5 / 8, round(5 / 8, 2))
>>>>>>> 9a266ba57eecbe187e5d2594b2bcd429b2658abe
