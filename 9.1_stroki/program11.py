"""
На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести число записанное в двоичной системе счисления.

Sample Input 1:
5

Sample Output 1:
101

Sample Input 2:
128

Sample Output 2:
10000000
"""
string = ''
n = int(input())
while n != 0:
    last_digit = n % 2
    string = str(last_digit)+string
    n = n // 2
print(string)
