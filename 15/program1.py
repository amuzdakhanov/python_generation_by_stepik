
"""

Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше")
Руслан может гарантированно угадать число Тимура?

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести наименьшее количество вопросов, которых гарантированно хватит Руслану, чтобы угадать число Тимура.


Sample Input 1:
8

Sample Output 1:
3

Sample Input 2:
20

Sample Output 2:
5

Sample Input 3:
100

Sample Output 3:
7


n = int(input())
counter =0
if n % 2 == 0:
    while n != 1:
        n=(n+1)//2
        counter = counter +1
else:
    while n != 0:
        n=(n)//2
        counter = counter +1
print(counter)


"""

n = int(input())
for i in range(1,n+1):
    if 2**i >= n:
        print(i)
        break
