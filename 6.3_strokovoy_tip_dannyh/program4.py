"""
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.
"""
city1,city2,city3 = input(), input(), input()
min_length = min(len(city1), len(city2), len(city3))
if len(city1) == min_length:
    print(city1)
elif len(city2) == min_length:
    print(city2)
else:
    print(city3)

max_length = max(len(city1), len(city2), len(city3))
if len(city1) == max_length:
    print(city1)
elif len(city2) == max_length:
    print(city2)
else:
    print(city3)
