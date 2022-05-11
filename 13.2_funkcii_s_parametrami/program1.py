"""
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

    fill – символ заполнитель;
    base – величина основания равнобедренного треугольника;

а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.

Sample Input 1:
*
9

Sample Output 1:
*
**
***
****
*****
****
***
**
*

"""      


def draw_triangle(fill,n):
    for i in range(n//2+1):
        for j in range(i+1):
            print(fill,end='')
        print()
    for i in range(n//2,0,-1):
        for j in range(i,0,-1):
               print(fill,end='')
        print()

fill = input()
n = int(input())
draw_triangle(fill, n)