# На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n×19

n = 7
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*'*19)
    else:
        print('*', ' '*17, '*', sep='')