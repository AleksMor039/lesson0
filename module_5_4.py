class House:
    houses_history = [] # В классе House создайте атрибут houses_history = [],
                        # который будет хранить названия созданных объектов.

    def __new__(cls, *args):               #Дополните метод __new__ так, чтобы:
        cls.houses_history.append(args[0]) #Название объекта добавлялось в список cls.houses_history.
        return object.__new__(cls)         #Название строения можно взять из args по индексу.


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):    # переопределите метод __del__(self) в котором будет выводиться строка:
                          # "<название> снесён, но он останется в истории"
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
h4 = House('Квартал Цветов', 33)
print(House.houses_history)

# Удаление объектов
del h2
del h3
del h4

print(House.houses_history)