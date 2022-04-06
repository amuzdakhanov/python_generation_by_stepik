"""
На вход программе подается натуральное число n.
Напишите программу вычисления знакочередующей суммы
1−2+3−4+5−6+…+(−1)^(n+1)*n.


Входные данные
На вход программе подается натуральное число nnn.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.
"""
n = int(input())
total_1 = 0
total_2 = 0
for i in range(1,n+1):
    if i % 2 != 0:
        total_1 = total_1 + i
    else:
        total_2 = total_2 - i
print(total_1 + total_2)