"""
На вход программе подается строка текста.
Напишите программу, которая выводит слова введенной строки в столбик.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input:
У лукоморья дуб зеленый златая цепь на дубе том

Sample Output:
У
лукоморья
дуб
зеленый
златая
цепь
на
дубе
том
"""
n = input()
s = n.split()
print(*s,sep='\n')