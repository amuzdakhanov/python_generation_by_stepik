"""
На вход программе подается натуральное число nnn, а затем nnn строк.
Напишите программу, которая создает из указанных строк список и выводит его.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести список состоящий из указанных строк.


Sample Input:
5
C#
C++
C
Python
F#

Sample Output:
['C#', 'C++', 'C', 'Python', 'F#']
"""
l = []
n = int(input())
for i in range(n):
    l.append(input())
print(l)
