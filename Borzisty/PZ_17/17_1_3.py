from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Анкета Web-разработчика')
root.geometry('400x400')
root.resizable(width=False, height=False)

title = Label(root, text='Анкета Web-разработчика', font=('Times New Roman', 20))
title.place(relx=0)

regname = Label(root, text='Регистрационное имя', font=('Times New Roman', 10), justify=LEFT).grid(row=0, column=0, sticky=W)
regname_entry = Entry(root).grid(row=0, column=1, padx=5, pady=5)

# passw = Label(root, text='Пароль', font=('Times New Roman', 10))
# passw.place(relx=0, rely=0.17)
# passw = Label(root, text='подтвердите пароль', font=('Times New Roman', 10))
# passw.place(relx=0.66, rely=0.22)
# passw_entry = Entry(root)
# passw_entry.place(relx=0.35, rely=0.17)
# passw_entry = Entry(root)
# passw_entry.place(relx=0.35, rely=0.22)

# spec = Label(root, text='Ваша специализация', font=('Times New Roman', 10))
# spec.place(relx=0, rely=0.29)
# www = ['Web-мастер', 'Web-ломастер']
# spec_entry = ttk.Combobox(values=www)
# spec_entry.place(relx=0.35, rely=0.29)

# gender = Label(root, text='Пол', font=('Times New Roman', 10))
# gender.place(relx=0, rely=0.36)
# radioM = Radiobutton(root, text='M')
# radioM.place(relx=0.35, rely=0.36)
# radioW = Radiobutton(root, text='Ж')
# radioW.place(relx=0.45, rely=0.36)


if __name__ == '__main__':
    root.mainloop()