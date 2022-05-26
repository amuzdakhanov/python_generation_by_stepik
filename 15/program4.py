"""
Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря с сдвигом вправо на 10 символов.

Примечание. Считайте, что русский алфавит состоит из 323232 букв (буква ё отсутствует).

"""

s = 'Блажен, кто верует, тепло ему на свете!'

shag = 10
for i in s:
    if 1040 <= ord(i) <= 1071 and ord(i) + shag <= 1071:
        n = ord(i)+shag
        print(chr(n),end='')
    elif 1072 <= ord(i) <= 1103 and ord(i) + shag <= 1103:
        n = ord(i)+shag
        print(chr(n),end='')
    elif 1040 <= ord(i) <= 1071 and ord(i) + shag > 1071:
        n = 1039+(shag - (90-ord(i)))
        print(chr(n),end='')
    elif 1072 <= ord(i) <= 1103 and ord(i) + shag > 1103:
        n = 1071+(shag - (122-ord(i)))
        print(chr(n),end='')
    else:
        print(i,end='')
