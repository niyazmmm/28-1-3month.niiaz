from aiogram import types, Dispatcher
from config import ADMINS, bot
import random
from database.bot_db import sql_command_all, sql_command_delete


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(message.from_user.id, f"id - {user['id']},\n"
                                                     f"имя - {user['name']},\nнаправление - {user['direction']},\n"
                                                     f"возраст - {user['age']}, \n "
                                                     f"группа - {user['group']}",
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"Удалить {user[1]}", callback_data=f"delete {user[0]}")))


async def delete_user(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(message.from_user.id,
                               f"id - {user[0]},name - {user[1]},dir - {user[2]}, "
                               f"age - {user[3]}, group - {user[4]}",
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"Delete {user[1]}", callback_data=f"delete {user[0]}")
                               ))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(int(call.data.replace('delete ', '')))
    await call.answer(text="Стёрт с базы данных", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_message_admin(dp: Dispatcher):
    dp.register_message_handler(delete_user, commands=["del"])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )


async def ban(message: types.Message):
@@ -33,4 +70,3 @@ async def game(message: types.Message):
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(game)
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько яблок на березе??"
    question = "Сколько областей в Кыргызстане?"
    answer = [
                 "12",
                 "3",
                 "БЕССКОНЕЧНОСТЬ",
                 "7",
                 "0",
                 "-10",
                 "999",
             @ @ -26, 7 + 26, 7 @ @ async

    def quiz_2(call: types.CallbackQuery):

        is_anonymous = False,
    type = 'quiz',
    correct_option_id = 2,
    explanation = "Стыдно не знать",
    explanation = "Стыдно не знать брат!",
    open_period = 5,
    reply_markup = markup

)

@ @-49

, 7 + 49, 7 @ @ async

def quiz_3(call: types.CallbackQuery):
    is_anonymous = False,
    type = 'quiz',
    correct_option_id = 3,
    explanation = "Стыдно не знать",
    explanation = "Стыдно не знать брат!",
    # open_period=5,

)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from keybort.client_kb import start_markup
from database.bot_db import sql_command_random, sql_command_all
from keybort.client_kb import direction_markup


# @dp.message_handler(commands=['start'])
@@ -14,13 +16,14 @@ async def pin_chat_command(message: types.Message):
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message_id=message.reply_to_message.message_id)
        else:
            await message.answer('сообщение должно быть ответом')
            await message.answer('Сообщение должно быть ответом умник!')
    else:
        await message.answer('пши в группе')
        await message.answer('Пиши в группе чел!')


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('Сам разбирайся')
    await message.answer('Сам разбирайся баурым!')


# @dp.message_handler(commands=['quiz'])
@@ -45,14 +48,22 @@ async def quiz_1(message: types.Message):
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        explanation="Стыдно не знать брат!",
        open_period=5,
        reply_markup=markup
    )

async def get_random_user(message: types.Message):
    # await message.answer("Какое направление?", reply_markup=direction_markup)
    await sql_command_random(message)


async def get_all_mentor(message: types.Message):
    await sql_command_all()
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_chat_command, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_random_user, commands=["getmentor"])
    dp.register_message_handler(get_all_mentor, commands=["allmentor"])
    quiz_button,
    help_button,

)
)
direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
direction_back = KeyboardButton("BackEnd")
direction_front = KeyboardButton("FrontEnd")
direction_uxui = KeyboardButton("UX UI")
direction_android = KeyboardButton("Android")
direction_ios = KeyboardButton("IOS")
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
submit_markup1 = KeyboardButton("ДА")
submit_markup2 = KeyboardButton("НЕТ")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))
direction_markup.add(direction_back, direction_front, direction_android).add(direction_uxui, direction_ios).add(
    KeyboardButton("CANCEL"))
submit_markup.add(submit_markup1, submit_markup2)