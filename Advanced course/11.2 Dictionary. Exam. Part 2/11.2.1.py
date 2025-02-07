# Как известно из курса биологии ДНК и РНК – последовательности нуклеотидов.
# Четыре нуклеотида в ДНК:
# аденин (A); цитозин (C); гуанин (G); тимин (T).
# Четыре нуклеотида в РНК:
# аденин (A); цитозин (C); гуанин (G); урацил (U).
# Цепь РНК строится на основе цепи ДНК последовательным присоединением комплементарных нуклеотидов:
# G → C; C → G; T → A; A → U.
# Напишите программу, переводящую цепь ДНК в цепь РНК.

s = input()
dnk_to_rnk = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}

print(*(dnk_to_rnk[i] for i in s), sep='')