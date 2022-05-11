"""
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. Проблема заключается в том, что данный метод не находит местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

Примечание 2. Следующий программный код:

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))

должен выводить:

[0, 4, 7, 8, 9]
[]
[4]
"""

def find_all(target, symbol):
    result = []
    for i  in range(len(target)):
        if symbol == target[i]:
            result.append(i) 
    return result
target = input()
symbol = input()
print(find_all(target,symbol))



