from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup

from core.conf import dp, settings
from utils import Sentence
from utils.decorators import check_user_existance


@dp.message_handler(Command("sentence"))
@check_user_existance
async def sentence(message: Message):
    markup = ReplyKeyboardMarkup(
        row_width=3,
        one_time_keyboard=True,
        resize_keyboard=True
    )

    for el in settings.LANGS:
        markup.insert(el)

    await message.answer("Выберите язык с которого хотите перевести", reply_markup=markup)
    await Sentence.dest.set()
