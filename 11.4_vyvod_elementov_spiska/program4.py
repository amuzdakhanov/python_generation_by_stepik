"""
На вход программе подается натуральное число nnn, а затем n строк.
Напишите программу, которая выводит только уникальные строки,
в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем n строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов.

Sample Input:
5
first
second
first
third
second

Sample Output:
first
second
third

"""
n = int(input())
l = []
for i in range(n):
    num = input()
    if num not in l:
        l.append(num)
print(*l,sep='\n')