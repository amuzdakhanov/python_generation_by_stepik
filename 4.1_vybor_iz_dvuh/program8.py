"""
Напишите программу, которая определяет наименьшее из четырёх чисел.

Формат входных данных
На вход программе подаётся четыре целых числа.

Формат выходных данных
Программа должна вывести наименьшее из четырёх чисел.

"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
minimum = num1
if num2 < minimum:
    minimum = num2
if num3 < minimum:
    minimum = num3
if num4 < minimum:
    minimum = num4
print(minimum)
