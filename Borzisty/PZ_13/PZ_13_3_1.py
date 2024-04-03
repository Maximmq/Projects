# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
import random
size = 4  # Размер квадратной матрицы
matrix = [[random.randint(10, 49) for i in range(size)] for i in range(size)]
print(*matrix, sep='\n', end='\n\n')


def double_diag(elem):
    return list(map(lambda i: list(map(lambda j: elem[i][j] * 2 if i == j else elem[i][j], range(len(elem[i])))), range(len(elem))))


print(*double_diag(matrix), sep='\n')