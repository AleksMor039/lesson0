import sys
import pprint
import requests
import inspect


def introspection_info(obj):
    # тип объекта
    ob_type = type(obj).__name__
    # атрибуты объекта
    attributes = dir(obj)
    # методы
    methods = [method for method in attributes if callable(getattr(obj, method))]
    # к какому модулю принадлежит
    module = inspect.getmodule(obj)
    # вывести в виде словаря
    answer = {'type': ob_type, 'attributes': attributes, 'methods': methods, 'module': module}

    return (answer)


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('Строка')
print(string_info)

list_info = introspection_info(['line', 32, True, 0.5])
print(list_info)
