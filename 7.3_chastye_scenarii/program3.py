"""
https://stepik.org/lesson/294243/step/7?unit=275922
Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.
"""
from  math import *
n = int(input())
total = 1
for i in range(2,n+1):
    total = total + (1/i)
total = total - log(n)
print(total)
