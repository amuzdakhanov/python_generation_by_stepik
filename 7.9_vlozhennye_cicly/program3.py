"""
На вход программе подается два натуральных числа a и b (a < b).
Напишите программу, которая находит натуральное число из отрезка [a; b] с максимальной суммой делителей.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и сумму его делителей.

Примечание. Если таких чисел несколько, то выведите наибольшее из них.


Sample Input 1:
1
10

Sample Output 1:
10 18

Sample Input 2:
1
100

Sample Output 2:
96 252
"""
a = int(input())
b = int(input())
max_sum_d = 1
max_n= 0
for i in range(a,b+1):
    sum_d = 0
    for j in range(1,b+1):
        if i % j == 0:
            sum_d=sum_d+j
        if sum_d >= max_sum_d:
            max_sum_d = sum_d
            max_n = i
print(max_n,max_sum_d)
