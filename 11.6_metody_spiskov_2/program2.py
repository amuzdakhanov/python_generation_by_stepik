#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
На вход программе подается строка текста, содержащая различные натуральные числа. 
Из данной строки формируется список чисел. 
Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

Формат входных данных
На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести строку текста в соответствии с условием задачи.

Примечание. Используйте подходящие встроенные функции и списочные методы.
"""

n = input()
s = n.split()
for i in range(len(s)):
    s[i] = int(s[i])
ind_max = s.index(max(s))
ind_min = s.index(min(s))
s[ind_min], s[ind_max] = s[ind_max], s[ind_min]
print(*s)