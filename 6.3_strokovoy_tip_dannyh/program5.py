"""
Вводятся 3 строки в случайном порядке. Напишите программу,
которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES»,
если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.
"""
str1,str2,str3 = input(), input(), input()
min_length = min(len(str1), len(str2), len(str3))
max_length = max(len(str1), len(str2), len(str3))
sum = len(str1) + len(str2) + len(str3)
sum_mm = min_length + max_length
avr_length = sum - sum_mm

if avr_length - min_length == max_length - avr_length:
    print('YES')
else:
    print('NO')
