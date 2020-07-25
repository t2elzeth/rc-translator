from aiogram.types import ChatActions, Message
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from data.config import ADMIN_ID

@dp.message_handler(CommandStart())
async def start(message: Message):
    db.user_id_exists()
    
    await ChatActions.typing()
    await message.reply("Привет\n\n\
Кто я?\n\
Я - бот который поможет тебе с переводами\n\n\
Что я умею?\n\
Вкратце: 'ЛУЧШИЙ БОТ В ТВОЕЙ ЖИЗНИ'\n\
    • 5 высших образований на педагога по-английскому (Ну яж бот, тыче ожидал)\n\
    • Миллион (вру) учеников довольных мною\n\
    • Мои ученики давно отправились в США и покоряют Hollywood и Silicone valley (как ни странно, снова вру)\n\n\
Ладно, давай серьезно:\n\
    • Поддерживаю перевод с 10, и на 10 языков мира.\n\
    • Сразу дам тебе 10+ примеров, чтобы все было понятнее\n\
    • Есть ежедневная обучающая рассылка, которая поможет тебе с обучением английского. Подробнее:\n\
        • Три новых слова\n\
        • 5 примеров к каждому слову\n\
        • И все это будет отправляться тебе каждый день по выбранному тобою графику\n\n\
Команды:\n\
    /word - перевести одно слово и получить тонну примеров с ним\n\
    /sentence - перевести предложение\n\
    /rating - посмотреть свою статистику\n\
    /setsub - изменить настройки подписки на 'обучалку'\n\n\
Твой статус подписки на обучающюю рассылку: `подписан`\n\
Твой нынешний режим обучения - №1\n\
Изменить все это можно по команде /setsub")
