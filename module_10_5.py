import multiprocessing
import datetime


def read_info(name):  # аргум. назв. файла
    all_data = []  # локал.список
    with open(name, 'r') as file:  # откр.для чтения
        while True: # цикл до тех пор пока строка не будет пустой
            line = file.readline()  # метод читает одну полн.строку
            all_data.append(line)  # считал - добавил в список
            if not line:
                break

# создать список названий файлов как в архиве
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный вызов # 0:00:02.929243 (линейный)

start = datetime.datetime.now()
for file in filenames:
    read_info(file)
end = datetime.datetime.now()
print(f'{end - start} (линейный)')

############################################################################################

# мультипроцессный вызов # 0:00:01.305528 (многопроцессный)

# if __name__ == '__main__':  # это проверка на то, что файл который запускается - основной(т.е. отделить от дочерних проц)
#     start = datetime.datetime.now()
#     with multiprocessing.Pool(processes=len(filenames)) as pool:  # Pool принимает аргументом количество процессов
#         pool.map(read_info, filenames)  # pool приним. 1м аргум.функцию которой каждый процесс будет заниматься,
#         # 2м аргум. приним список
#     end = datetime.datetime.now()
#     print(f'{end - start} (многопроцессный)')
