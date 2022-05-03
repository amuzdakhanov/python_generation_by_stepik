
"""
Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали, 
и любезно соглашается помочь им в решении их проблем. 
Одной из такой проблем являлся странный компьютерный вирус, 
который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. 
Известно, что программисты Братства никогда не оставляют комментарии к коду, и пишут программы на Python, 
поэтому удаление всех этих комментариев никак не навредит им. Помогите писцу Ибсену удалить все комментарии из программы.

Формат входных данных
На первой строке вводится символ решётки и сразу же натуральное число nnn — количество строк в программе, не считая первой. 
Далее следует n строк кода.

Формат выходных данных
Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк. 
Пустую строку вместо первой строки ввода выводить не надо.



Sample Input:
#12
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)         #долой Макнамару
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)          #Элайджа вперёд
else:
    print("Здравствуйте, послушник", name)

Sample Output:
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)
else:
    print("Здравствуйте, послушник", name)


"""

n = input()
n = int(n.replace('#', ''))
s = []
for i in range(n):
    string = input().rstrip()
    if '#' in string:
        index = string.find('#')
        string = string[0:index].rstrip()
    s.append(string)
print(*s,sep='\n')
