"""
На вход программе подается строка текста.
Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если длина строки нечетная, то длина первой части должна быть на один символ больше.

Sample Input 1:
abcdef

Sample Output 1:
defabc

Sample Input 2:
abcdefg

Sample Output 2:
efgabcd

Sample Input 3:
a

Sample Output 3:
a
"""
s = input()
len_s = len(s)
if  len_s % 2 == 0 :
    p1 = int(len_s / 2)
    p2 = p1
else:
    p1 = int(len_s//2 + 1)
    p2 = len_s - p1

if len_s == 1:
    print(s)
else:
    print(s[-p2:],s[:p1],end='',sep='')

#=============решение2================
s = input()
len_s = len(s)
p1 = len_s//2 + len_s%2
p2 = len_s - p1
if len_s == 1:
    print(s)
else:
    print(s[-p2:],s[:p1],end='',sep='')
