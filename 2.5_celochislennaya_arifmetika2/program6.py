"""
Напишите программу для пересчёта величины временного интервала,
заданного в минутах, в величину, выраженную в часах и минутах.

Формат входных данных
На вход программе подаётся целое число – количество минут.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
n = int(input())
h = n//60
m = n%60
print(n, 'мин - это', h, 'час', m, 'минут.' )
