"""
Напишите программу, которая определяет наименьшее из двух чисел.

Формат входных данных
На вход программе подаётся два различных целых числа.

Формат выходных данных
Программа должна вывести наименьшее из двух чисел.

"""
num1 = int(input())
num2 = int(input())
test = 0

if num1 > num2:
    test = num2
else:
    test = num1
print(test)