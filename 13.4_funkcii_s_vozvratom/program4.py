
"""
Напишите функцию number_of_factors(num), 
принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

Примечание 2. Следующий программный код:

print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))

должен выводить:

1
2
4
"""


def get_factors(num):
    list = []
    for i in range(1,num+1):
        if num%i == 0:
           list.append(i)
    return list
def number_of_factors(num):
    return len(get_factors(num))
num = int(input())

print(number_of_factors(num))