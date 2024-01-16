'''
Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно заменив символы третей
строки их числовыми кодами.
'''
import string
with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_11\\text18-3.txt', 'r+', encoding='utf-16') as text:
    tt = text.read()
    print('\n' + tt, '\n')
    text.seek(0)
    four = ' '.join([next(text) for _ in range(4)])
    text.seek(0)
    th = text.readlines()[2]
    three = list(th)
print(f'Кол-во знаков пунктуации в первых 4 строках: {sum([four.count(i) for i in string.punctuation])}')

for i in three[:-1]:
    three[three.index(i)] = ord(i)
new = tt.replace(th, str(three)[1:][:-7] + '\n')

with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_11\\text2.txt', 'w+', encoding='utf-16') as fin:
    fin.write(new)