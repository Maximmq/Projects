'''
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9
'''
# Дан символ C. Вывести два символа, первый из которых предшествует символу C в
# кодовой таблице, а второй следует за символом C

from tkinter import *


def get_symbols():
    try:
        C = ord(entry.get())
        result = f"Предыдущий символ: {chr(C-1)}, Следующий символ: {chr(C+1)}"
    except TypeError:
        result = 'Неправильный ввод!'
    result_label.config(text=result)


root = Tk()
root.title("Символы")
root.geometry('400x300')

prog = Label(root, text='Программа для вывода предыдущего и следующего символа')
prog.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Получить символы", command=get_symbols)
button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
