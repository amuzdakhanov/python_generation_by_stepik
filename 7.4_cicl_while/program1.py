"""
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Концом последовательности является слово «КОНЕЦ» (без кавычек). Напишите программу,
которая выводит члены данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести члены данной последовательности.
"""
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()
