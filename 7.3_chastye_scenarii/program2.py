"""
На вход программе подается натуральное число nnn, а затем nnn целых чисел, каждое на отдельной строке.
Напишите программу, которая подсчитывает сумму введенных чисел.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму данных чисел.
"""
n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total += num
print(total)
