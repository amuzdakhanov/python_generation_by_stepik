from random import *
digits='0123456789'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation='!#$%&*+-=?@^_'

chars = ''

pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')

if pwd_digits == 'да':
    chars +=  digits
if pwd_uppercase == 'да':
    chars +=  uppercase_letters
if pwd_lowercase == 'да':
    chars +=  lowercase_letters
if pwd_punctuation == 'да' :
    chars +=  punctuation
if pwd_exceptions.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(pwd_len, chars):
    password = ''
    for j in range(pwd_len):
        password += choice(chars)
    return password

for _ in range(pwd_quantity):
   print( generate_password(pwd_len, chars))
