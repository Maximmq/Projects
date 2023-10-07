def skidka():
    cena = int(input("Введите стоимость продуктов (1-2000): "))
    if 0 < cena <= 500:
        print("Скидка 2%")
    elif 500 < cena <= 1000:
        print("Скидка 3%")
    elif 1000 < cena <= 1500:
        print("Скидка 4%")
    elif 1500 < cena <= 2000:
        print("Скидка 5%")
    else:
        skidka()
skidka()