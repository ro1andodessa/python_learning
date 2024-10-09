# Словарь программиста 📘
# Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

# Формат входных данных
# В первой строке задано одно целое число n — количество слов в словаре. В следующих n строках записаны слова и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число m — количество поисковых слов, чье определение нужно вывести. В следующих m строках записаны сами слова, по одному на строке.

# Формат выходных данных
# Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение. Если слова в словаре нет, программа должна вывести «Не найдено» (без кавычек).

# Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть по ссылке.

# Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (':'), следом за которым идёт пробел.

# Тестовые данные 🟢

# Sample Input 1:

# 5
# Змея: язык программирования Python
# Баг: от англ. bug — жучок, клоп, ошибка в программе
# Конфа: конференция
# Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
# Бета: бета-версия, приложение на стадии публичного тестирования
# 3
# Змея
# Жаба
# костыль

# Sample Output 1:

# язык программирования Python
# Не найдено
# код, который нужен, чтобы исправить несовершенство ранее написанного кода

slang_dict = {}

for n in range(int(input())):
    t = input().split(': ')
    slang_dict.setdefault(t[0].lower(), t[1])

print(*(slang_dict.get(input().lower(), 'Не найдено') for i in range(int(input()))), sep='\n')
