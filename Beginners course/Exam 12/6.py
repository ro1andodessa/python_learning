# Молодежный жаргон

# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая преобразует каждое слово введенного текста в «молодежный жаргон» по следующему правилу:

# первая буква каждого слова удаляется и ставится в конец слова;
# затем в конец слова добавляется слог «ки».

# Формат входных данных
# На вход программе подается строка текста на русском языке.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# s = input().split()
# [i + i[0] +'ки' for i in s]
print(*[(i + i[0] + "ки")[1:] for i in input().split()])
# print(*[i[1:] + i[0] + "ки"for i in input().split()])
