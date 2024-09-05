from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'  # инкапсулир.атрибут

    def get_products(self):  # Метод
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')  # открываем файл
        products = file.read()  # выполняем действие
        # (считываем всю инф.из файла __file_name)
        file.close()  # закрываем файл

        return products  # и возвращает единую строку
        # со всеми товарами из файла __file_name.

    def add(self, *products):  # метод
        for product in products:
            if product.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(product.__str__() + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
