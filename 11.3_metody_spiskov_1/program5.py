"""
На вход программе подается натуральное число n.
Напишите программу, которая создает список состоящий из делителей введенного числа.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести список, состоящий из делителей введенного числа.

Sample Input 1:
17

Sample Output 1:
[1, 17]

Sample Input 2:
25

Sample Output 2:
[1, 5, 25]

Sample Input 3:
36

Sample Output 3:
[1, 2, 3, 4, 6, 9, 12, 18, 36]
"""

n = int(input())
l = []
for i in range(1,n+1):
    if n % i == 0:
        l.append(i)
print(l)