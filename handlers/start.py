from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from core.settings import dp
from utils.decorators import typing_action, check_user_existance


@dp.message_handler(CommandStart())
@typing_action
@check_user_existance
async def start(message: Message):
    await message.reply("""Привет
    
Кто я?
Я - бот который поможет тебе с переводами

Что я умею?
Вкратце: 'ЛУЧШИЙ БОТ В ТВОЕЙ ЖИЗНИ'
    • 5 высших образований на педагога по-английскому (Ну яж бот, тыче ожидал)
    • Миллион (вру) учеников довольных мною
    • Мои ученики давно отправились в США и покоряют Hollywood и Silicone valley (как ни странно, снова вру)
    
Ладно, давай серьезно:
    • Поддерживаю перевод с 10, и на 10 языков мира.
    • Сразу дам тебе 10+ примеров, чтобы все было понятнее
    • Есть ежедневная обучающая рассылка, которая поможет тебе с обучением английского. Подробнее:
        • Три новых слова
        • 5 примеров к каждому слову
        • И все это будет отправляться тебе каждый день по выбранному тобою графику
        
Как переводить?
Чтобы перевести, просто напиши без комманд:
    • Одно слово, и получишь примеры
    • Предложение, и получишь перевод на 5 языков
    
Команды:
    /grammar - помощники по всей грамматике английского
    /rating - посмотреть свою статистику
    /setsub - изменить настройки подписки на 'обучалку'
    
Твой статус подписки на обучающюю рассылку: `подписан`
Твой нынешний режим обучения - №1
Изменить все это можно по команде /setsub""")
