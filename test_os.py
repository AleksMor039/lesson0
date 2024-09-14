import os
import time

print('Текущая директория:', os.getcwd())
print(os.listdir())
for i in os.walk('.'):
    print(i)
os.chdir(r'C:\Users\admin\PycharmProjects\python_test\direct_1')
print('Текущая директория:', os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)

directory = '.'

for root, dirs, files in os.walk(directory):  # для просмотра вложенных директорий ( '.' означает текущая директория)
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        abs_path = os.path.abspath(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}, Абсолютный путь: {abs_path}')






