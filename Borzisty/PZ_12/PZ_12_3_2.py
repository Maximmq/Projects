'''
Составить генератор (yield), который выводит из строки только цифры.
'''


def gener(stroka):
    for i in stroka:
        if i.isdigit():
            yield i


stroka = input('Введите строку: ')
for i in gener(stroka):
    print(i)
