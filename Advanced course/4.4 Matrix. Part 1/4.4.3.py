# След матрицы
# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

# Формат выходных данных
# Программа должна вывести одно число — след заданной матрицы.

# Тестовые данные 🟢
# Sample Input 1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
# 15

# Sample Input 2:
# 4
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
# Sample Output 2:
# 4

n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(num) for num in input().split()])

print(sum(matrix[i][i] for i in range(n)))