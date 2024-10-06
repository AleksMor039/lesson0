import threading
import random
import time
from queue import Queue


class Table:
    def __init__(self, number):  # номер стола  - это число
        self.number = number  # атрибут - номер стола
        self.guest = None  # атрибут - гость


class Guest(threading.Thread):  # поток т.к. наследуется от Thread
    def __init__(self, name):  # имя гостя - строка
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))  # ожидание случ.образом


class Cafe:
    def __init__(self, *tables):  # столы в кафе любая коллекция
        self.queue = Queue()  # атрибут очередь
        self.tables = list(tables)  # объекты класса - это список столов

    def guest_arrival(self, *guests): # метод - прибытие гостей
        for guest in guests:
            table = self.find_free_table()
            if table:
                table.guest = guest  # назначить столу guest
                guest.start()  # запуск потока гостя
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):  # метод - имитация процесса обслуживания гостей
        while not self.queue.empty() or self.any_guest_still_seated(): # работа пока есть очередь или хоть 1 стол с гостем
            for table in self.tables:
                if table.guest and not table.guest.is_alive(): # проверка гостя (потока) и поток не жив
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None # текущий стол освобождается

                if not self.queue.empty() and table.guest is None: # проверка пуста ли очередь и сбободен ли стол
                    next_guest = self.queue.get() # взять след.гостя из очереди
                    table.guest = next_guest # текущему столу присвоить гостя взятого из очереди
                    next_guest.start()
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

    def find_free_table(self): # поиск свободного или освободившегося стола
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def any_guest_still_seated(self): # поиск гостя 
        return any(table.guest is not None for table in self.tables)


# Создание столов через списковую сборку
tables = [Table(number) for number in range(1, 6)]
# Список гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# создание гостей через списковую сборку
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
