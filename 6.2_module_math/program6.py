"""
Даны три вещественных числа a, b, c. Напишите программу,
которая находит вещественные корни квадратного уравнения
ax**2+bx+c=0.

Формат входных данных
На вход программе подается три вещественных числа a≠0, b, c, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.

Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

"""
from  math import *
a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4*a*c
if D>0:
    x1 = (-b - sqrt(D))/(2*a)
    x2 = (-b + sqrt(D))/(2*a)
    x_min = min(x1, x2)
    x_max = max(x1, x2)
    print(x_min, x_max, sep='\n')
elif D == 0:
    x = (-b)/(2*a)
    print(x)
else:
    print('Нет корней')
