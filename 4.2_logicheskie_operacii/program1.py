"""
Напишите программу, которая принимает целое число x и определяет,
принадлежит ли данное число указанному промежутку.

Формат входных данных
На вход программе подаётся целое число xxx.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
https://stepik.org/lesson/265083/step/8?unit=246031
"""
num = int(input())
if 17 > num > -1:
    print('Принадлежит')
else:
    print('Не принадлежит')
