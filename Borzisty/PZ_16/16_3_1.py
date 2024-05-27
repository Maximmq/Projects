'''
Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
инкремента и декремента значения. Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
'''
import pickle


class Counter:

    def __init__(self, curr_val):
        self.curr_val = curr_val

    @staticmethod
    def incr(vel):
        vel += 1
        return vel

    @staticmethod
    def decr(vel):
        vel -= 1
        return vel


def save_def(val, file):
    with open(file, 'wb') as f:
        pickle.dump(val, f)


def load_def(file):
    with open(file, 'rb') as f:
        val = pickle.load(f)
    return val


a = Counter(0)
b = Counter(1)
c = Counter(2)


val_info = [a, b, c]

for val in val_info:
    save_def(val, 'values.pkl')
    values = load_def('values.pkl')
    print(values.incr(values.curr_val))
    print(values.decr(values.curr_val), '\n')
