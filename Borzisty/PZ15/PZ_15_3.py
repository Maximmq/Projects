'''
Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
Преподавательский состав должна содержать следующие данные: Табельный номер,
Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата
'''

import sqlite3 as sq
from prepsos import info_prepods

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS teaching_staff")
    cur.execute("CREATE TABLE IF NOT EXISTS teaching_staff("
                "tab_n INTEGER PRIMARY KEY AUTOINCREMENT,"
                "fio TEXT NOT NULL,"
                "birthday DATE NOT NULL,"
                "position TEXT NOT NULL,"
                "degree BOOLEAN NOT NULL,"
                "load TEXT NOT NULL,"
                "salary INTEGER NOT NULL)")

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO teaching_staff VALUES(?,?,?,?,?,?,?)", info_prepods)


with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM teaching_staff WHERE load=='Средняя'")
    result_1 = cur.fetchall()
    print(*result_1, sep='\n', end='\n\n')

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM teaching_staff WHERE salary>20000")
    result_2 = cur.fetchall()
    print(*result_2, sep='\n', end='\n\n')

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM teaching_staff WHERE degree=TRUE")
    result_3 = cur.fetchall()
    print(*result_3, sep='\n', end='\n\n')


with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE teaching_staff SET position='Директор' WHERE degree==TRUE AND load=='Высокая' ")
    cur.execute("SELECT * FROM teaching_staff WHERE position='Директор'")
    result_4 = cur.fetchall()
    print(*result_4, sep='\n', end='\n\n')

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE teaching_staff SET degree=TRUE WHERE degree==False")
    cur.execute("SELECT * FROM teaching_staff")
    result_5 = cur.fetchall()
    print(*result_5, sep='\n', end='\n\n')

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE teaching_staff SET salary=0 WHERE load='Низкая'")
    cur.execute("SELECT * FROM teaching_staff")
    result_6 = cur.fetchall()
    print(*result_6, sep='\n', end='\n\n')


with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM teaching_staff WHERE salary>24000")
    cur.execute("SELECT * FROM teaching_staff")
    result_7 = cur.fetchall()
    print(*result_7, sep='\n', end='\n\n')

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM teaching_staff WHERE birthday NOT LIKE '2%'")
    cur.execute("SELECT * FROM teaching_staff")
    result_8 = cur.fetchall()
    print(*result_8, sep='\n', end='\n\n')

with sq.connect('kafedra.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM teaching_staff WHERE load=='Средняя'")
    cur.execute("SELECT * FROM teaching_staff")
    result_9 = cur.fetchall()
    print(*result_9, sep='\n', end='\n\n')
