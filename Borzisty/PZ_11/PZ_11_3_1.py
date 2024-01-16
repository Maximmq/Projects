'''
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Минимальный элемент:
Квадраты четных элементов:
Сумма квадратов четных элементов:
Среднее арифметическое суммы квадратов четных элементов:
'''
from random import randint
with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_11\\file.txt', 'w+') as file:
    # Создаём файл и записываем в него 10 случайных чисел
    file.write(' '.join(str([randint(-100, 100) for i in range(10)])[1:][:-1].split(", ")))
with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_11\\file.txt', 'r+') as file:
    # Открываем этот же файл на чтение и преобразуем его в int
    sti = list(map(int, file.read().split()))

sq = []

for i in sti:
    if int(i) % 2 == 0:
        i = int(i)**2
        sq.append(i)

with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_11\\itog.txt', 'w+') as itog:
    itog.write('Исходные данные: ' + str(sti)[1:][:-1] + '\n')
    itog.write('Кол-во элементов: ' + str(len(sti)) + '\n')
    itog.write('Минимальный элемент: ' + str(min(sti)) + '\n')
    itog.write('Квадраты четных элементов: ' + str(sq)[1:][:-1] + '\n')
    itog.write('Сумма квадратов четных элементов: ' + str(sum(sq)) + '\n')
    itog.write(f'Среднее арифметическое суммы квадратов четных элементов:  {sum(sq) / len(sq):.3f}')
