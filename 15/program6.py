"""
Текст "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг." был получен в результате шифрования алгоритмом Цезаря с сдвигом вправо на 777 символов. Расшифруйте данный текст.

Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).
"""

s = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'

shag = 7
for i in s:
    if 1040 <= ord(i) <= 1071 and ord(i) - shag >= 1040:
        n = ord(i)-shag
        print(chr(n),end='')
    elif 1072 <= ord(i) <= 1103 and ord(i) - shag >= 1072:
        n = ord(i)-shag
        print(chr(n),end='')
    elif 1040 <= ord(i) <= 1071 and ord(i) - shag < 1040:
        n = 1072 - (shag-(ord(i)-1040))
        print(chr(n),end='')
    elif 1072 <= ord(i) <= 1103 and ord(i) - shag < 1072:
        n = 1104 - (shag-(ord(i)-1072))
        print(chr(n),end='')
    else:
        print(i,end='')
