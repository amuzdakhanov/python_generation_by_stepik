"""
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка состоит из 26 символов z.
"""

l = []
for i in range(1,27):
    for j in range(97,123):
        l.append(i*chr(j))
        i = i+1
    break
print(l)

###################2-е решение ##############
l = []
for i in range(26):
        l.append(chr(ord('a') + i)*(i+1))
print(l)
