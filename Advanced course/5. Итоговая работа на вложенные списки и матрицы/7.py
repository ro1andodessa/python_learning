# Ходы ферзя
# На шахматной доске 8 × 8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните точками.

# Формат входных данных
# На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номер строки (цифра от 1 до 8, снизу вверх)).

# Формат выходных данных
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
# '''

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

coord = input()
x = 8 - int(coord[1])
y = 'abcdefgh'.index(coord[0])
matrix = [['.'] * 8 for _ in range(8)]

for i in range(8):
    matrix[x][i] = '*'
    matrix[i][y] = '*'
    for j in range(8):
        if i - j == x - y or  i + j == x + y:
            matrix[i][j] = '*'
matrix[x][y] = 'Q'

for row in matrix:
    print(*row)




# 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# n = 4
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 3],
#     [8, 9, 6, 2],
#     [4, 8, 5, 1]]
# n = 4
# matrix =[
#     [1, 3, 4, 2],
#     [2, 4, 1, 3],
#     [3, 1, 2, 4],
#     [4, 2, 3, 1]]
# seq = [i for i in range(1, n + 1)]
# is_lat = 'YES'
# s_row = []

# for i in range(n):
#     s_col = []
#     for j in range(n):
#         s_col.append(matrix[j][i])
#     print(s_col)
#     s_row = matrix[i].copy()
#     s_row.sort()
#     s_col.sort()    
#     print(f'i = {i}; j = {j}; seq = {seq} ; s_row = {s_row} ; s_col = {s_col}')
#     if s_row != seq or s_col != seq:
#         is_lat = 'NO'
#         break
        
# print(is_lat)






# pos_str = input()
# chess = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# x = 8 - int(pos_str[1])
# y = chess.index(pos_str[0])

# matrix = [['.'] * 8 for _ in range(8)]
# matrix[x][y] = 'Q'

# for i in range(8):
#     for j in range(8):
#         if ((abs(x - i) > 0 and abs(y - j) == 0) or
#                 (abs(x - i) == 0 and abs(y - j) > 0) or
#                 (abs(x - i) == abs(y - j) != 0)):
#             matrix[i][j] = '*'
#         print(matrix[i][j], end=' ')
#     print()