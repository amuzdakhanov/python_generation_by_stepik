"""
На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

Формат входных данных
На вход программе подается строка текста. Текст может содержать строчные и заглавные буквы английского и русского алфавита, а также цифры.

Формат выходных данных
Программа должна вывести символ, который появляется наиболее часто.

Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.

Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.

Sample Input 1:
aaaabbc

Sample Output 1:
a

Sample Input 2:
abaabbcccc

Sample Output 2:
c
"""
s = input()
len_s = len(s)
b = 0
max = 0
for i in s:
    if s.count(i) >= b:
        b = s.count(i)
        max = i
print(max)
