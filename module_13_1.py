"""Задача Асинхронные силачи
Д/з Асинхронность на практике"""

import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')  # строка в нач.работы
    for i in range(5):  # цикл в пять шаров
        num_ball = i + 1
        await asyncio.sleep(i * 5 / power)  # для задержки асинхр. ф-ии
        print(f'Силач {name} поднял {num_ball} шар')  # строка после задержки пропорц.силе
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Паша', 3))
    task2 = asyncio.create_task(start_strongman('Денис', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1, task2, task3  # поставить каждую задачу в ожидание (await)


asyncio.run(start_tournament())  # запуск асинхр. ф-ии методом run
