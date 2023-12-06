# Дан список размера N (N — четное число). Поменять местами его первый элемент
# со вторым, третий — с четвертым и т. д.
try:
    N = list(map(float, input('Введите cписок через пробел: ').split()))
    for j in range(0, len(N)-1, 2):
        N[j], N[j+1] = N[j+1], N[j]
    print(N)
except ValueError:
    print('Неверный ввод!')
