"""
На вход программе подается натуральное число n. Напишите программу,
которая подсчитывает сумму тех чисел от 1 до n (включительно)
квадрат которых оканчивается на 2, 5 или 8.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Если таких чисел нет в указанном диапазоне, то следует вывести 0.
"""

n = int(input())
total = 0
for i in range(1, n+1):
    if (i**2)%10 == 2 or (i**2)%10 == 5 or (i**2)%10 == 8:
        total = total + i
print(total)
