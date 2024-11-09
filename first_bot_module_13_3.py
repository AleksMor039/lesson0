import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "Нео, ключ возьмёшь у ключника."
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# это так....для прикола...было хорошее настроение
# @dp.message_handler(text=['что ты умеешь', 'как сохранить здоровье'])
# async def questions_message(message):
#     print('Вопросики однако :)')
#     await message.answer('Как Бот - пока ничего не умею, не пей не кури и будет тебе счастье.')


@dp.message_handler(commands=['start'])
async def start(message):
    print('Поступила команда на старт - ключ на старт')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_messages(message):
    print('Мы получили сообщение!')
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
