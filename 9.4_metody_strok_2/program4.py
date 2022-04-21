"""
На вход программе подается строка текста.
Напишите программу, которая подсчитывает количество цифр в данной строке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести количество цифр в данной строке.
Тестовые данные 🟢

Sample Input 1:
nezabud dl-6

Sample Output 1:
1

Sample Input 2:
l33t 3301

Sample Output 2:
6
"""
s = input()
counter = 0
len_s = len(s)
for i in range(len_s):
    if s[i] in '0123456789':
        counter += 1
print(counter)
#=============2-решение===============

s = input()
counter = 0
for i in range(10):
        counter += s.count(str(i))
print(counter)
