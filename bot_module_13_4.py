"""Д/З по теме "Машина состояний"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "ключник отдал ключ Нео. Ищите Нео, он где-то в матрице"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

"""ф-ия по отработке команды /start"""


@dp.message_handler(commands=['start'])
async def start(message):
    print('Поступила команда на старт - ключ на старт')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


"""создание класса с 3-мя объектами"""


class UserState(StatesGroup):
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес


"""отработка кода по установлению возраста"""


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()  # ожидает ввода возраста


"""отработка кода по установлению роста"""


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()  # ожидает ввода роста


"""отработка кода по установлению веса"""


@dp.message_handler(state=UserState.growth)
async def set_weigt(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()  # ожидает ввода веса


"""отработка кода по расчёту нормы калорий"""


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = int(10 * weight + 6.25 * growth - 5 * age + 5)  # формула Миффлина-Сан Жеора (для мужчин)
    await message.answer(f"Ваша норма калорий: {calories} Ккал в день")
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    print('Мы получили сообщение!')
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
