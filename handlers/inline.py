import random

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
@@ -22,6 +24,17 @@ async def pin_chat_command(message: types.Message):
        await message.answer('Пиши в группе чел!')


async def send_audio(message: types.Message):
    audios = (
        'media/50_Cent_x_Скриптонит_x_Andy_Panda_Привычка_Kerim_Remix_.mp3',
        'media/RMR-DEALER-feat-Future-Lil-Baby-Official-Music-Video.m4a',
        'media/Su x Worth It [BADAYTOFF TIK TOK EDIT].mp3',
        'media/Врываемся.mp3',
        'media/Скриптонит_x_Truwer_Животные_edit_by_8kenshi.mp3',
    )
    audio = open(random.choice(audios), 'rb')
    await bot.send_audio(message.chat.id, audio=audio)

# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('Сам разбирайся баурым!')
@@ -83,5 +96,6 @@ def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_chat_command, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_random_user, commands=["getmentor"])
    dp.register_message_handler(send_audio, commands=["music"])
    dp.register_message_handler(get_all_mentor, commands=["allmentor"])
    dp.register_message_handler(parsser_wheels, commands=["wheel"])