"""
https://stepik.org/lesson/298796/step/6?unit=280623
Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значение суммы 1!+2!+3!+…+n!.

Примечание 1. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть

"""
n = int(input())
total = 1
sum = 0
for i in range(1, n+1):
    total = total * i
    sum = sum + total
print(sum)

#2-е решение
n = int(input())
sum = 0
mul = 1
for i in range(1,2):
    for j in range(1,n+1):
        mul=i*j*mul
        sum = mul+sum
print(sum)
