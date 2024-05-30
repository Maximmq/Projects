'''
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9
'''
# Дана строка, содержащая строчные латинские буквы. Если буквы в строке
# упорядочены по алфавиту, то вывести 0; в противном случае вывести номер
# первого символа строки, нарушающего алфавитный порядок

from tkinter import *

def check_string():
    stroka = entry.get().lower()
    try:
        for i in range(len(stroka)-1):
            if ord(stroka[i]) > ord(stroka[i+1]):
                result.set('Символ, нарушающий порядок: '+str(i+1))
                return
        result.set('0')
    except ValueError:
        result.set('Неправильный ввод!')

root = Tk()
root.title("Порядок")
root.geometry('400x300')

prog = Label(root, text='Программа для проверки алфавитного порядка латиницы')
prog.pack()

entry = Entry(root)
entry.pack()

result = StringVar()
result_label = Label(root, textvariable=result)
result_label.pack()

button = Button(root, text='Проверить', command=check_string)
button.pack()

root.mainloop()
