"""
Текст "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
был получен в результате шифрования алгоритмом Цезаря со сдвигом вправо на 25 символов.
Расшифруйте данный текст.
"""

s = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'

shag = 25
for i in s:
    if 65 <= ord(i) <= 90 and ord(i) - shag >= 65:
        n = ord(i)-shag
        print(chr(n),end='')
    elif 97 <= ord(i) <= 122 and ord(i) - shag >= 97:
        n = ord(i)-shag
        print(chr(n),end='')
    elif 65 <= ord(i) <= 90 and ord(i) - shag < 65:
        n = 91 - (shag-(ord(i)-65))
        print(chr(n),end='')
    elif 97 <= ord(i) <= 122 and ord(i) - shag < 97:
        n = 123 - (shag-(ord(i)-97))
        print(chr(n),end='')
    else:
        print(i,end='')
