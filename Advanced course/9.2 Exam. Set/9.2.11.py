# Онлайн-школа BEEGEEK 6 🌶️
# Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала учебного года. Для каждого урока есть листок со списком присутствовавших учеников.
# Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.
# Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
# Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.

# Формат входных данных
# На вход программе в первой строке дается число m - количество уроков, проведенных с начала учебного года. Далее идет m блоков строк, описывающих листки с фамилиями. На первой строке каждого блока указано количество фамилий n i-ое, затем идет n строчек с фамилиями тех, кто был на i-ом уроке.

# формат выходных данных
# Программа должна вывести фамилии учеников, которые были на всех уроках, отсортированных в лексикографическом порядке. Каждая фамилия должна быть записана на отдельной строке.

m = int(input())
res = {input() for _ in range(int(input()))}
for i in range(m - 1):
    set1 = {input() for _ in range(int(input()))}
    res &= set1
print(*sorted(res), sep='\n')
