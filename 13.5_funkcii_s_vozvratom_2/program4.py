"""
Напишите функцию is_password_good(password), 
которая принимает в качестве аргумента строковое значение пароля password и 
возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

    его длина не менее 8 символов; 
    он содержит как минимум одну заглавную букву (верхний регистр); 
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.

 Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

должен выводить:

True
False
"""

def is_password_good(password):
    length = len(password)
    if length < 8: 
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for i in password:
        if i in '0123456789':
            flag1 = True
        elif i == i.upper():
            flag2 = True
        elif i == i.lower():
            flag3 = True
    return (flag1 and flag2 and flag3)
txt = input()

# вызываем функцию
print(is_password_good(txt))     

"""
def is_password_good(password):
    length = len(password)
    if length < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for i in password :
        if i.isupper():
            flag1 = True
        elif i.islower():
            flag2 = True
        elif i.isdigit():
            flag3 = True
    return (flag1 and flag2 and flag3)
        
            
            
        
        
txt = input()

# вызываем функцию
print(is_password_good(txt))             
         """       
                