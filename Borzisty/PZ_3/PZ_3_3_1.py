# нужно проверить истинность высказывания, является ли число А чётным
try:
    A = int(input("Введите целое число: "))
    print("Число А является чётным:", A % 2 == 0)
except ValueError:
    print("Вы не ввели целое число!")