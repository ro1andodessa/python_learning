# Negatives, Zeros and Positives
# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# n = [int(input()) for _ in range(int(input()))]
n = [3, -4, 1, 0, -1, 0, -2]
print(*[i for i in n if i < 0], sep='\n')
print(*[i for i in n if i == 0], sep='\n')
print(*[i for i in n if i > 0], sep='\n')