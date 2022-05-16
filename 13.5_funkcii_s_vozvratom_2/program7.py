"""
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. 
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.

Напишите функцию is_valid_password(password), 
которая принимает в качестве аргумента строковое значение пароля password и 
возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False
"""
def is_prime(num):

    flag = True
    if num == 1 :
        flag = False
    else:    
        for i in range(2,num):
            if num % i == 0:
                flag = False
                break
    return flag
def is_palindrome(text):
    return text == text[::-1]

def is_valid_password(password):
    password = [i for i in password.split(':')]
    if len(password)!=3:
        return False
    else:
        flag1 = False
        flag2 = False
        flag3 = False
        password[1]=int(password[1])
        password[2]=int(password[2])
        if is_palindrome(password[0]) == True:
            flag1 = True
        if is_prime(password[1]) == True:
            flag2 = True
        if password[2] % 2 == 0:
            flag3 = True
        return (flag1 and flag2 and flag3)


txt = input()
print(is_valid_password(txt))
