#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите функцию is_prime(num), 
которая принимает в качестве аргумента натуральное число 
и возвращает значение True если число является простым и False в противном случае.

Примечание. Следующий программный код:

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))

должен выводить:

False
False
True
"""
def is_prime(num):
    flag = True
    if num == 1 :
        flag = False
    else:    
        for i in range(2,num):
            if num % i == 0:
                flag = False
                break
    return flag

num = int(input())
print(is_prime(num))