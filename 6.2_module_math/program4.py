"""
Напишите программу, вычисляющую значение тригонометрического выражения
sin⁡x+cos⁡x+(tan⁡x)**2
по заданному числу градусов x.

Формат входных данных
На вход программе подается одно вещественное число xxx измеряемое в градусах​.

Формат выходных данных
Программа должна вывести одно число – значение тригонометрического выражения.

Примечание 1. Тригонометрические функции принимают аргумент в радианах. Чтобы перевести градусы в радианы, воспользуйтесь формулой
r=x⋅π/180 


Примечание 2. Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.
https://stepik.org/lesson/265110/step/5?unit=246058
"""
from  math import *
x = float(input())
x = radians(x)
s = sin(x) + cos(x)+(tan(x))**2
print(s)
