# Заполнение 2
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n × m, заполнив её в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

# Тестовые данные 🟢
# Sample Input 1:
# 3 7
# Sample Output 1:
# 1  4  7  10 13 16 19      3*7 - 2     n*m - k = n - 1
# 2  5  8  11 14 17 20      3*7 - 1
# 3  6  9  12 15 18 21      3*7 - 0

# Sample Input 2:
# 6 6
# Sample Output 2:
# 1  7  13 19 25 31
# 2  8  14 20 26 32
# 3  9  15 21 27 33
# 4  10 16 22 28 34
# 5  11 17 23 29 35
# 6  12 18 24 30 36

# 🟢🟢🟢🟢🟢🟢 Main 🟢🟢🟢🟢🟢🟢

n, m = [int(_) for _ in input().split()]
matrix = []

for i in range(n):
    matrix.append([i + j * n + 1  for j in range(m)])
    print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))

    


# # 🤔🤔🤔🤔 Test 🤔🤔🤔🤔

# 1 4 7 10
# 2 5 8 11
# 3 6 9 12

# n, m = 3, 4
# matrix = []
# print(n, m)

# for i in range(n):
#     k = n - 1
#     matrix.append([i + j + 1  for j in range(0, n * m - k + 1, n)])
#     k -= 1
#     # print(' '.join(str(matrix[i][j]).ljust(3) for j in range(m)))
# print(*matrix, sep='\n')