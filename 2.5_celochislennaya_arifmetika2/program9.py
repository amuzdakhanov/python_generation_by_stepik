"""
Напишите программу для нахождения цифр четырёхзначного числа.

Формат входных данных
На вход программе подаётся положительное четырёхзначное целое число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""



n = int(input())
a = str(n//1000)
b = str((n%1000)//100)
c = str((n%100)//10)
d = str(n%10)
print('Цифра в позиции тысяч равна',a)
print('Цифра в позиции сотен равна',b)
print('Цифра в позиции десятков равна',c)
print('Цифра в позиции единиц равна',d)
