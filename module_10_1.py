# импорты необходимых модулей и функций
from time import sleep
from threading import Thread
from datetime import datetime


# объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)  # выставили паузу записи
    print(f'Завершилась запись в файл {file_name}')


# взятие текущего времени
start_time_f = datetime.now()
# запуск ф-ии с аргум.из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# взятие текущего времени после выполн. ф-ии
end_time_f = datetime.now()
# вывод разницы начала и конца раб. ф-ии
function_time = end_time_f - start_time_f
print(f'Работа функций {function_time}')

# взятие текущего времени перед созд. и запуском потоков
start_time_thr = datetime.now()
# создание и запуск потоков с аргументами из задачи
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
# взятие текущего времени
end_time_thr = datetime.now()
# вывод разницы нач. и конца раб. потоков
thread_time = end_time_thr - start_time_thr
print(f'Работа потоков {thread_time}')
