# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
import random
size = 4  # Размер квадратного массива
matrix = [[random.randint(10, 49) for i in range(size)] for i in range(size)]
print(*matrix, sep='\n', end='\n\n')
for i in range(size):
    matrix[i][i] *= 2
print(*matrix, sep='\n')
