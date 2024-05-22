'''
Создайте класс "Автомобиль", который содержит информацию о марке, модели и
годе выпуска. Создайте класс "Грузовик", который наследуется от класса
"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
информацию о количестве пассажиров.
'''


class Auto:
    def __init__(self, manuf, model, year):
        self.manuf = manuf
        self.model = model
        self.year = year


mashina = Auto('Koenigsegg', 'Agera', 2011)


class Truck(Auto):
    def __init__(self, manuf, model, year, lift):
        super().__init__(manuf, model, year)
        self.lift = lift


truck = Truck('Kamaz', 'Kakoito', 2000, '1500kg')


class Car(Auto):
    def __init__(self, manuf, model, year, passan):
        super().__init__(manuf, model, year)
        self.passan = passan


car = Car('Lada', 'Priora', 2005, 4)
