# Ходы коня 🐎
# На шахматной доске 8 × 8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьёт конь. Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые бьёт конь, отметьте символами *, остальные клетки заполните точками.

# Формат входных данных
# На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 1 до 8, снизу вверх)).

# Формат выходных данных
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

# Тестовые данные 🟢
# Sample Input 1:
# b6
# Sample Output 1:
# * . * . . . . .
# . . . * . . . .
# . N . . . . . .
# . . . * . . . .
# * . * . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .

# Sample Input 2:
# f3
# Sample Output 2:
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . * . * .
# . . . * . . . *
# . . . . . N . .
# . . . * . . . *
# . . . . * . * .

# 🟢🟢🟢🟢🟢   Main     🟢🟢🟢🟢🟢

# horse = input()
# chessboard = []
# col = 'abcdefgh'
# row ='87654321'

# horse_coord = [int(row.index(horse[1])), int(col.index(horse[0]))]

# chessboard = [['.'] * 8 for i in range(8)]

# chessboard[horse_coord[0]][horse_coord[1]] = 'N'

# for i in range(8):
#     for j in range(8):
#         if abs(i - horse_coord[0]) * abs(j - horse_coord[1]) == 2:
#             chessboard[i][j] = '*'

# for row in chessboard:
#     print(' '.join(map(str, row)))




# 🤔🤔🤔🤔🤔    Test    🤔🤔🤔🤔🤔

horse = 'b6'
col = 'abcdefgh'
row ='87654321'
horse_coord = [int(row.index(horse[1])), int(col.index(horse[0]))]
print(horse_coord)

chessboard = [['.'] * 8 for i in range(8)]

chessboard[horse_coord[0]][horse_coord[1]] = 'N'

for i in range(8):
    for j in range(8):
        if abs(i - horse_coord[0]) * abs(j - horse_coord[1]) == 2:
            chessboard[i][j] = '*'

for row in chessboard:
    print(' '.join(map(str, row)))

