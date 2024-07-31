# 1. Функция с параметрами по умолчанию
def print_params (a=1, b='строка', c=True):
    print(a, b, c)
print_params()
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(2, 'home')
print_params(b=25)
print_params(c=[1, 2, 3])
print()
# 2. Распаковка параметров
values_list = ['небо', 3.14, (25, 50)]
values_dict = {'a': 8, 'b': False, 'c': "земля"}
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
# (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
#print_params(*values_list, **values_dict) объединённый вызов и распаковка не могут быть произведены
# т.к. у функции print_params 3 аргумента, а при распаковке списка и словаря получится 6 элементов
print()
# 3. Распаковка + отдельные параметры
#Создайте список values_list_2 с двумя элементами разных типов
#Проверьте, работает ли print_params(*values_list_2, 42)
values_list_2 = ['дерево', 1.20]
print_params(*values_list_2, 42)