"""
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
Напишите программу, которая выводит инициалы человека.

Формат входных данных
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input:
Владимир Семенович Высоцкий

Sample Output:
В.С.В.


"""
n = input()
s = n.split()
for i in range(3):
    print(*s[i][0],end='.')