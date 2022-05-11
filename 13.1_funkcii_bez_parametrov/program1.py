"""
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×1014 \times 1014×10 в соответствии с образцом:

**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
"""

def draw_box():
    print ('**********')
    for i in range (12) : print ('*        *')
    print ('**********')
draw_box()

"""
def draw_box():
    for i in range(14):
       for j in range(10):
           if i == 0 or i == 13:
               print('*',end='')
           elif j == 0 or j == 9:
               print('*',end='        ')
       print()

draw_box()
"""