# Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса. Каждый день Тимур решает ровно две сложные математические задачи. Решая первую задачу, он записывает на первом листочке все числа, которые в ней встречаются. Далее он делает паузу и берется за вторую задачу. Затем записывает на втором листочке все числа, которые в ней встречаются. После этого он берет еще один листок и выписывает на него все совпадающие числа из первых двух листочков. Если такие числа есть, день удался, если общих чисел нет, Тимур считает день неудачным.
# Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏

# На вход программе подаются две строки с числами - первая с числами с первого листка, вторая со второго.

set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}

print(*(sorted(set1 & set2, reverse = True) if set1 & set2 else ['BAD DAY']))

