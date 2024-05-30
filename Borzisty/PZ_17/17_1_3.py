'''
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу
'''

from tkinter import *
from tkinter import ttk


def delete():
    regname_entry.delete(0, 'end')
    passw_entry.delete(0, 'end')
    passww_entry.delete(0, 'end')
    spec_entry.delete(0, 'end')
    skills2.delete(1.0, 2.0)
    HTMSCSS.deselect()
    Perl.deselect()
    ASP.deselect()
    Photoshop.deselect()
    JAVA.deselect()
    JavaScript.deselect()
    Flash.deselect()


def reg():
    g = 'Ж' if r_var.get() else 'М'

    with open('user.txt', 'w+') as f:
        f.write('Name: '+regname_entry.get()+'\n')
        f.write('Password: '+passw_entry.get()+'\n')
        f.write('Specialization: '+spec_entry.get()+'\n')
        f.write('Gender: '+g+'\n')
        f.write('HTML & CSS: '+str(var1.get())+'\n')
        f.write('Perl: '+str(var2.get())+'\n')
        f.write('ASP: '+str(var3.get())+'\n')
        f.write('Photoshop: '+str(var4.get())+'\n')
        f.write('JAVA: '+str(var5.get())+'\n')
        f.write('JavaScript: '+str(var6.get())+'\n')
        f.write('Flash: '+str(var7.get())+'\n')
        f.write('Additional info: '+skills2.get(1.0, 'end')+'\n')


root = Tk()

root.title('Анкета Web-разработчика')
root.geometry('510x450')
root.resizable(width=False, height=False)

regname = Label(root, text='Регистрационное имя', font=('Times New Roman', 10)).grid(row=1, column=0, sticky='w')
regname_entry = Entry(root)
regname_entry.grid(row=1, column=1, padx=5, pady=5, sticky='e')

passw = Label(root, text='Пароль', font=('Times New Roman', 10)).grid(row=2, column=0, sticky='w')
passww = Label(root, text='подтвердите пароль', font=('Times New Roman', 10)).grid(row=3, column=2, sticky='w')
passw_entry = Entry(root, show="•")
passw_entry.grid(row=2, column=1, padx=5, sticky='e')
passww_entry = Entry(root, show="•")
passww_entry.grid(row=3, column=1, padx=5, sticky='e')

spec = Label(root, text='Ваша специализация', font=('Times New Roman', 10)).grid(row=4, column=0, sticky='w')
www = ['Web-мастер', 'Web-ломастер']
spec_entry = ttk.Combobox(values=www)
spec_entry.grid(row=4, column=1, padx=5, pady=5, sticky='e')

gender = Label(root, text='Пол', font=('Times New Roman', 10)).grid(row=5, column=0, sticky='w')
r_var = BooleanVar()
r_var.set(False)
radioM = Radiobutton(root, text='Ж', variable=r_var, value=True)
radioM.grid(row=5, column=1, padx=51, pady=5, sticky='w')
radioW = Radiobutton(root, text='М', variable=r_var, value=False)
radioW.grid(row=5, column=1, padx=5, pady=5, sticky='w')

var1, var2, var3, var4, var5, var6, var7 = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()
skills = Label(root, text='Ваши навыки', font=('Times New Roman', 10))
skills.grid(row=6, column=0, sticky='w')
HTMSCSS = Checkbutton(root, text='знание HTML и CSS', font=('Times New Roman', 10), variable=var1)
HTMSCSS.grid(row=6, column=1, padx=5, sticky='w')
Perl = Checkbutton(root, text='знание Perl', font=('Times New Roman', 10), variable=var2)
Perl.grid(row=7, column=1, padx=5, sticky='w')
ASP = Checkbutton(root, text='знание ASP', font=('Times New Roman', 10), variable=var3)
ASP.grid(row=8, column=1, padx=5, sticky='w')
Photoshop = Checkbutton(root, text='знание Adobe Photoshop', font=('Times New Roman', 10), variable=var4)
Photoshop.grid(row=9, column=1, padx=5, sticky='w')
JAVA = Checkbutton(root, text='знание JAVA', font=('Times New Roman', 10), variable=var5)
JAVA.grid(row=10, column=1, padx=5, sticky='w')
JavaScript = Checkbutton(root, text='знание JavaScript', font=('Times New Roman', 10), variable=var6)
JavaScript.grid(row=11, column=1, padx=5, sticky='w')
Flash = Checkbutton(root, text='знание Flash', font=('Times New Roman', 10), variable=var7)
Flash.grid(row=12, column=1, padx=5, sticky='w')

skills = Label(root, text='Дополнительные', font=('Times New Roman', 10))
skills.grid(row=13, column=0, sticky='nw')
skills = Label(root, text='сведения о себе', font=('Times New Roman', 10))
skills.grid(row=13, column=0, sticky='w')

skills2 = Text(root, height=4, width=25)
skills2.grid(row=13, column=1, sticky='w', padx=5)

zareg = Button(text='зарегистрировать', command=reg)
zareg.grid(row=14, column=0, padx=10, pady=10, sticky='ns')
clear = Button(text='очистить форму', command=delete)
clear.grid(row=14, column=1, padx=10, pady=10, sticky='w')

if __name__ == '__main__':
    root.mainloop()
