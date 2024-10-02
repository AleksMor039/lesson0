import threading
import random
import time
from threading import Thread, Lock


class Bank(Thread): # создали класс Bank наследующий от класса Thread упр.и мониторинг потоков
    def __init__(self):
        self.balance = 0 # баланс банка (int)
        self.lock = Lock() # объект класса Lock - для блокировки
        super().__init__()


    def deposit(self):
        for i in range(100): # будет совершать 100 транзакций
            if self.balance >= 500 and self.lock.locked(): # если баланс больше или равен 500
                                                           # и замок заблокирован
                self.lock.release() # разблокировать методом release
            refill = random.randint(50, 500) # пополнение - увел.баланса на случ.число от 50 до 500
            self.balance += refill
            print(f'Пополнение: {refill}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100): # будет совершать 100 транзакций
            withdrawal = random.randint(50, 500) # Снятие - уменьш.баланса на случ.число от 50 до 500
            print(f'Запрос на {withdrawal}')
            if self.balance >= withdrawal:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)
bk = Bank() # созд.объект класса Bank + 2 потока для его методов
            # deposit и take

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
