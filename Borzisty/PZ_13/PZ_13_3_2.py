'''
Из матрицы сформировать массив из положительных четных элементов,
найти их сумму и среднее арифметическое.
'''
import random
size = 4  # Размер квадратного массива
massiv = []
matrix = [[random.randint(-99, 99) for i in range(size)] for i in range(size)]
print(*matrix, sep='\n', end='\n\n')
for i in matrix:
    for j in i:
        if j >= 0 and j % 2 == 0:
            massiv.append(j)
try:
    print(f'{massiv}{'\n'}Сумма: {sum(massiv)}\
        {'\n'}Среднее арифм.: {sum(massiv)/len(massiv):.3f}')
except ZeroDivisionError:
    print('Чётных положительных нет')
