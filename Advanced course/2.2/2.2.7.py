# Камень, ножницы, бумага
# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

# Формат входных данных
# На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.

# Формат выходных данных
# Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.

# 1	    камень  бумага	Руслан
# 2	    камень  камень	ничья
# 3	    камень  ножницы	Тимур

# Решение версии 1.
choices = ['камень', 'ножницы', 'бумага']
timurs_choice, ruslans_choice = 'бумага', 'бумага'
# timurs_choice, ruslans_choice = input(), input()
if timurs_choice == ruslans_choice:
    print('ничья')
elif (timurs_choice == 'камень' and ruslans_choice == 'ножницы') or (timurs_choice == 'ножницы' and ruslans_choice == 'бумага') or (timurs_choice == 'бумага' and ruslans_choice == 'камень'):
    print('Тимур')
else:
    print('Руслан')

# Решение версии 2.
options = ["камень", "ножницы", "бумага"]
results = ["ничья", "player2", "player1"]
# выигрышь игрока1 - выигрышь игрока2 
# -1
# -1
# 2 - всегда на последний элемент
# проигрышь игрока1 - выигрышь игрока2
# -2
# 1
# -2 - всегда на средний элемент (он же второй с конца)


player1 = input()
player2 = input()

case = options.index(player1) - options.index(player2)
res = results[case]

print(res)