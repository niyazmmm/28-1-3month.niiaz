from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from hw4.bot_db import sql_command_insert
from config import bot, ADMINS
from keyboards.clien_kb import direction_markup, submit_markup, cancel_markup

@@ -43,7 +43,7 @@ async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какое направление?", reply_markup=direction_markup)
    await bot.send_message(message.from_user.id, "Какое направление?", reply_markup=direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
@@ -55,35 +55,38 @@ async def load_direction(message: types.Message, state: FSMContext):

async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Из какой группы?", reply_markup=cancel_markup)

        if 50 > int(message.text) > 12:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Из какой группы?", reply_markup=cancel_markup)
        else:
            await message.answer("возраст не подходит")
    except:
        await message.answer("Вводи только числа!")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, f"{data['id']}"
                                                     f"{data['name']}, {data['direction']}, {data['age']}, "
                                                     f"{data['group']}")
        await bot.send_message(message.from_user.id, f"id - {data['id']},\n"
                                                     f"имя - {data['name']},\nнаправление - {data['direction']},\nвозраст - {data['age']}, \n"
                                                     f"группа - {data['group']}")

    await FSMAdmin.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # Запись в БД
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Регистрация завершена")
    if message.text.lower() == 'нет':
        await bot.send_message(message.from_user.id, "Регистрация завершена")
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer('Не получилось!')


async def cancel_reg(message: types.Message, state: FSMContext):