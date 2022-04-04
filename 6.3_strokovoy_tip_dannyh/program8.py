"""
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
Напишите программу проверяющую корректность email адреса.

Формат входных данных
На вход программе подаётся одна строка – email адрес.

Формат выходных данных
Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.

Примечание. Наличие символов @ и . недостаточно для корректности email адреса,
однако их отсутствие гарантировано влечёт за собой неверный email.
"""
str = input()
if '@' not in str and '.' not  in str:
    print('NO')
else:
    print('YES')
