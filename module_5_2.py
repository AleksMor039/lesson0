class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # __len__(self) - должен возвращать кол - во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors

    # __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Светлый квартал', 11)
# __str__
print(h1)
print(h2)
print(h3)
# __len__
print(len(h1))
print(len(h2))
print(len(h3))
