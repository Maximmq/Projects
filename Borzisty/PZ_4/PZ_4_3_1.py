# Дано вещественное число - цена 1 кг конфет. Вывести
# стоимость 1, 2, ..., 10 кг конфет
try:
    cena = float(input("Введите цену за кг: "))
    for i in range(1, 11):
        print(f'Цена за {i} кг: {i * cena}')
except ValueError:
    print('Вы не ввели число!')
