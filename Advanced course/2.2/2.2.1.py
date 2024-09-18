def quadrant(x, y):
    abs_x = abs(x)
    abs_y = abs(y)
    return [[abs_x, abs_y], [-abs_x, abs_y], [-abs_x, -abs_y], [abs_x, -abs_y]].index([x, y]) + 1

counter = [0, 0, 0, 0]
n = int(input())

for i in range(n):
    x_y = input().split()
    if int(x_y[0]) != 0 and int(x_y[1]) != 0:
        counter[quadrant(int(x_y[0]), int(x_y[1])) - 1] += 1

print('Первая четверть:', counter[0])
print('Вторая четверть:', counter[1])
print('Третья четверть:', counter[2])
print('Четвертая четверть:', counter[3])

# 4
# 0 -1
# 1 2
# 0 9
# -9 -5
