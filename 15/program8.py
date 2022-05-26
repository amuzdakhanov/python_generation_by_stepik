"""
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.

Формат входных данных
На вход программе подается строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.
Sample Input 1:

Day, mice. "Year" is a mistake!

Sample Output 1:
Gdb, qmgi. "Ciev" ku b tpzahrl!

Sample Input 2:
my name is Python!

Sample Output 2:
oa reqi ku Veznut!
"""

def cifr_ceaser(s,shag):
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
    print(end=' ')

l = input().split()
len_l = len(l)
l_words = []
for i in range(len_l):
    shag = 0
    for j in l[i]:
       if  j.isalpha() :
           shag += 1
    l_words.append(shag)
for k in range(len_l):
    cifr_ceaser(l[k],l_words[k])
