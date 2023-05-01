import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("ID получен!")


async def go_to_geek():
    await bot.send_message(chat_id=chat_id, text="сегодня в 16:00 будет урок в Geektech!")


async def scheduler():
    aioschedule.every().wednesday.at('13:00').do(go_to_geek)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_id, lambda word: "напомни" in word.text)