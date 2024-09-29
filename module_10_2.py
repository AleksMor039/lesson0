from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        self.kname = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.kname}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.kname} сражается {days} день(дня), осталось {enemies} воинов врага.')
        print(f'{self.kname} одержал победу спустя {days} дней(я)!')


# Создание класса
knight_1 = Knight('Sir Lancelot', 10)
knight_2 = Knight('Sir Galahad', 20)
# Запуск потоков и остановка текущего
knight_1.start()
knight_2.start()
knight_1.join()
knight_2.join()
# Вывод строки об окончании сражения
print('Все битвы завершены! Враг разгромлен!')
