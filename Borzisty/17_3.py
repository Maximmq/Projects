'''
Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
оформленный согласно требованиям. Все задания выполняются c использованием модуля
OS:
1. перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
вложенных подкаталогов выводить не нужно.
2. перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
файлов в папке test.
3. перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
консоль. Использовать функцию basename () (os.path.basename()).
4. перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
привязанной к нему программе. Использовать функцию os.startfile().
5. удалить файл test.txt.
'''

import os

# Задание 1
os.chdir('.\\PZ_11')
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(files)

# Задание 2
os.chdir('..')
os.makedirs('test/test1')
os.rename('PZ_6/PZ_6_3_1.py', 'test/PZ_6_3_1.py')
os.rename('PZ_6/PZ_6_3_2.py', 'test/PZ_6_3_2.py')
os.rename('PZ_7/PZ_7_3_1.py', 'test/test1/PZ_7_3_1.py')
os.rename('test/test1/PZ_7_3_1.py', 'test/test1/test.txt')

for file in os.listdir('test'):
    print(f"{file}: {os.path.getsize(os.path.join('test', file))} bytes")

# Задание 3
os.chdir('PZ_11')
files = os.listdir('.')
shortest_file = min(files, key=len)
print(os.path.basename(shortest_file))
os.chdir('..')

# Задание 4
os.chdir(".\\reports")
os.startfile('PZ_17.pdf')
os.chdir('..')

# Задание 5
# os.remove(".\\test\\test1\\test.txt")
