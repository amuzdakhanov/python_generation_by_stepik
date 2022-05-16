#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

должен выводить:

this_is_camel_cased
is_prime_number
"""

# объявление функции
def convert_to_python_case(text):
    s = text[0]
    for i in text[1:]:
        if i.isupper():
            s = s + '_' + i
        else:
            s = s + i
    return s.lower()
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
