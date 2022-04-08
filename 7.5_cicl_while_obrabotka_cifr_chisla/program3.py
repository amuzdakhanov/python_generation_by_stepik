"""
Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надпись
"""


n = int(input())
maximum = 0
minimum = 9
while n != 0:
    last_digit = n % 10
    if last_digit > maximum:
        maximum = last_digit
    if last_digit < minimum :
        minimum = last_digit
    n = n // 10
print('Максимальная цифра равна',maximum)
print('Минимальная цифра равна',minimum)

"""
n = input()
maximum = max(n)
minimum = min(n)
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)
"""
