'''
Из матрицы сформировать массив из положительных четных элементов,
найти их сумму и среднее арифметическое.
'''
import random
size = 4  # Размер квадратной матрицы
massiv = []
matrix = [[random.randint(-9, 9) for i in range(size)] for i in range(size)]
print(*matrix, sep='\n', end='\n\n')


def polch(elem):
    for i in elem:
        for j in i:
            if j > 0 and j % 2 == 0:
                yield j


try:
    a = polch(matrix)
    for i in a:
        massiv.append(i)
    print(f'{massiv}{'\n'}Сумма: {sum(massiv)}\
        {'\n'}Среднее арифм.: {sum(massiv)/len(massiv):.3f}')
except ZeroDivisionError:
    print('Чётных положительных нет')
