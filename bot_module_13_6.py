"""Д/З по теме "Инлайн клавиатуры"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "*******"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

'''Инлайн клавиатура с 2мя кнопками'''
kb_inl = InlineKeyboardMarkup()
button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inl.add(button_1, button_2)


class UserState(StatesGroup):
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес


@dp.message_handler(commands=['start'])
async def start(message):
    print('Поступила команда на старт - ключ на старт')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")  # исп.клв в отв. ф-ии /start


'''нов. ф-ия main_menu(message)'''


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inl)


'''нов. ф-ия get_formulas(call)'''


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;'
                              '\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()  # сохранение кликабельности


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()  # сохранение кликабельности
    await UserState.age.set()  # ожидает ввода возраста


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()  # ожидает ввода роста


@dp.message_handler(state=UserState.growth)
async def set_weigt(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()  # ожидает ввода веса


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
