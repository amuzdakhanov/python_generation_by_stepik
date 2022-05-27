"""
Зашифруйте текст "To be, or not to be, that is the question!" алгоритмом Цезаря с сдвигом вправо на 17 символов.
"""
s = 'To be, or not to be, that is the question!'

shag = 17
for i in s:
    if 65 <= ord(i) <= 90 and ord(i) + shag <= 90:
        n = ord(i)+shag
        print(chr(n),end='')
    elif 97 <= ord(i) <= 122 and ord(i) + shag <= 122:
        n = ord(i)+shag
        print(chr(n),end='')
    elif 65 <= ord(i) <= 90 and ord(i) + shag > 90:
        n = 64+(shag - (90-ord(i)))
        print(chr(n),end='')
    elif 97 <= ord(i) <= 122 and ord(i) + shag > 122:
        n = 96+(shag - (122-ord(i)))
        print(chr(n),end='')
    else:
        print(i,end='')
