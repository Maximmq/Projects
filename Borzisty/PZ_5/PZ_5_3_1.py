# Составить функцию, которая выполнит суммирования числового ряда
def rsum(a, s):
    print(f'Сумма ряда: {sum([i * s for i in range(a + 1)]):.3f}')


try:
    amo = int(input('Введите кол-во шагов: '))
    step = float(input('Введите шаг: '))
    rsum(amo, step)
except ValueError:
    print('Неверный ввод!')
