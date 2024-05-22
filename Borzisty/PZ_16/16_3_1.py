import pickle


class Counter:

    def __init__(self, curr_val):
        self.curr_val = curr_val

    def incr(self):
        self.curr_val += 1

    def decr(self):
        self.curr_val -= 1

    def val(self):
        return self.curr_val

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
print(a.val())
a.incr()
a.incr()
print(a.val())
c.decr()
print(c.val())

val_info = [a, b, c]

for val in val_info:
    save_def(val, 'values.pkl')
    values = load_def('values.pkl')
    print(values)