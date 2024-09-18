# Сумма чисел

# На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Строковый метод join() работает только со списком строк.
# s = ['2 2 2']
s = list(map(int, input().split()))

print(*(_ for _ in s), sep="+", end="\n")
print(sum(s))
