"""
Дано трехзначное число abc, в котором все цифры различны. Напишите программу,
которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число,
все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел,
образованных при перестановке цифр заданного числа в следующем порядке: abc, acb, bac, bca, cab, cba
"""

n = int(input())
a = str(n//100)
b = str((n%100)//10)
c = str(n%10)
print(a+b+c,a+c+b,b+a+c,b+c+a,c+a+b,c+b+a,sep='\n')
