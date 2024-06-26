'''Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
86532547891), а во второй с некорректными номерами телефонов. Посчитать
полученные строки в каждом файле.'''
import re

cf1, cf2 = 0, 0
with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_14\\hotline.txt', 'r+', encoding='utf-8') as f:
    for line in f:
        a = re.search(r'\d{11}$', line)
        if a:
            with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_14\\f1.txt', 'a+', encoding='utf-8') as f1:
                f1.write(line)
                cf1 += 1
        else:
            with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_14\\f2.txt', 'a+', encoding='utf-8') as f2:
                f2.write(line)
                cf2 += 1
print(f'Корректные: {cf1}{'\n'}Некорректные: {cf2}')
