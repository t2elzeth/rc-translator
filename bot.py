"""
Файл bot.py - каркасс из разных функций, собранных их разных модулей


Все функции для обработки команд в файле command_handler.py
Все функции для обработки callback'ов в файле callback_handler.py
Все функции по работе с БД прописаны в классе Sqlighter в файле myclass.py
Все дополнительные/вспомогательные функции в файле mymodule.py

Все классы в файле myclass.py

Все нужные константы в config.py

Инициализация необходимых переменных в loader
"""
# import required libraries
import logging
import schedule

# import from aiogram
from aiogram import executor
from aiogram.types import Message, CallbackQuery

# import from my files
from loader import dp, db
from command_handler import *
from callback_handler import *
from utils import States

# Configure logging
logging = logging.basicConfig(level=logging.INFO)
db.create_table()

@dp.message_handler(commands="start")
async def procces_send_welcome(message: Message):
    await send_welcome(message)

@dp.message_handler(commands="translate") # Тут выберется язык для перевода
async def procces_translate(message: Message):
    await command_translate(message)

@dp.message_handler(state=States.all()[0])
async def process_state_choose_lang_into(message: Message):
    await state_choose_lang_into(message)


@dp.message_handler(state=States.all()[1])
async def process_state_choose_lang_into(message: Message):
    await state_send_word(message)

@dp.message_handler(state=States.all()[2])
async def process_state_send_word(message: Message):
    await state_send_result(message)



# Handle all inline-buttons
@dp.callback_query_handler(lambda c: c.data == "show_examples")
async def process_show_examples(callback_query: CallbackQuery):
    await show_examples(callback_query)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
