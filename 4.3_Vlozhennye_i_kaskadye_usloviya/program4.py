"""
Дан порядковый номер месяца (1, 2, ..., 12). Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.

Примечание. Постарайтесь написать программу, так чтобы в ней было не более трех условий.

Формат входных данных
На вход программе подаётся одно целое число – порядковый номер месяца.

Формат выходных данных
Программа должна вывести количество дней в этом месяце.
"""
n = int(input())
if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print('31')
elif n == 4 or n == 6 or n == 9 or n == 11:
    print('30')
else:
    print('28')
