# Дана строка, содержащая строчные латинские буквы. Если буквы в строке
# упорядочены по алфавиту, то вывести 0; в противном случае вывести номер
# первого символа строки, нарушающего алфавитный порядок
try:
    stroka = input('Введите строку: ').lower()
    for i in range(len(stroka)-1):
        if ord(stroka[i]) >= ord(stroka[i+1]):
            print(stroka.index(stroka[i]))
            exit()
    print(0)
except ValueError:
    print('Неправильный ввод!')