"""
Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
"""
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
summ = 0
for i in range(len(numbers)):
    summ += numbers[i]**2
print(summ)
