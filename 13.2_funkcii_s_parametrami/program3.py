
"""
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
Тестовые данные 🟢

Sample Input 1:

12345

Sample Output 1:

15

Sample Input 2:

12

Sample Output 2:

3

Sample Input 3:

7

Sample Output 3:

7


"""

def print_digit_sum(n):
    summ = 0
    while n != 0:
        last_digit = n % 10
        summ = summ + last_digit
        n = n // 10
    print(summ)

any_num = int(input())
print_digit_sum(any_num)