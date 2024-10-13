import requests
import pandas as pd
import numpy as np
from pprint import pprint




""" Requests - библиотека в Python, позволяет взаимодействовать с веб ресурсами
большой набор функций для работы со всеми видами HTTP-запросов.
"""
# 1 задача по request - запросить данные с сайта и вывести их в консоль
d_url = {'name_1': 'https://api.github.com', 'name_2': 'https://ru.freepik.com',
         'name_3': 'https://site.ru/asdfjkl', 'name_4': 'https://api.tutiempo.net'}
for v in d_url.values():
    res = requests.get(v)
    print(res)
    r = res.status_code
    if res.status_code == 200:
        print('Нашёл сервер он отвечает и готов работать')
    elif res.status_code == 404:
        print('Ничего не найдено')
    elif res.status_code != 200:
        print('Что-то нашёл, работать не готов')
#
weather = requests.get('https://api.tutiempo.net')
json_flag = False
if weather.ok:
    try:
        weather = weather.json()
    except requests.exceptions.JSONDecodeError as e:
        print('Ответ не в формате json.', 'Был получен следующий ответ:',
              weather, sep='\n')
    else:
        json_flag = True
pprint(weather)
""" Pandas - это программная библиотека для обработки и анализа данных. 
Она предоставляет специальные структуры данных и операции для манипулирования числовыми таблицами и временны́ми рядами.
"""
# 2 задача по pandas - считать данные из файла,
# выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
series_example = pd.Series([4, 7, -5, 3])  # создаём объект Series, содержащий числа.
print(series_example)
print()
city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
        'Год основания': [1147, 1703, 1893, 1723],
        'Население': [11.9, 4.9, 1.5, 1.4]}  # словарь с необх.информацией
df = pd.DataFrame(city) # создаём объект DataFrame
print(df)
print()
food = {'Fruits': ['Манго', 'Яблоко', 'Банан', 'Апельсин'],
        'Quantity': [40, 20, 25, 10],
        'Price': [80, 100, 50, 70]}
df_2 = pd.DataFrame(food)
print(df_2)
print()
df_2 = df_2.sort_values('Fruits', ascending=True) # сортировка по названию
print(df_2)
print()
# работа с файлом .csv
students = pd.read_csv("Students_Performance.csv")
print(students.head())
print(students.tail(3))


