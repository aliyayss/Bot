from config import bot, dp
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def question1(message:types.Message):
    markup = InlineKeyboardMarkup()
    b1=InlineKeyboardButton(text='next', callback_data='next1')
    markup.add(b1)

    q='ferrari or ford'
    v=['ferrari','ford']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=q,
        options=v,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Под индексом 1',
        open_period=60,
        reply_markup=markup,
    )

async def question2(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    b1=InlineKeyboardButton(text='next', callback_data='next2')
    markup.add(b1)
    q = 'coffee or tea?'
    v = ['coffee', 'tea']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=q,
        options=v,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Под индексом 0',
        open_period=60,
        reply_markup=markup,
    )

async def question3(call:types.CallbackQuery):
    q = 'frontend or backend'
    v = ['frontend', 'backend']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=q,
        options=v,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Под индексом 1',
        open_period=60,
    )
def register_quiz(dp: Dispatcher):
    dp.register_message_handler(question1, commands=['quiz'])
    dp.register_callback_query_handler(question2, text='next1')
    dp.register_callback_query_handler(question3, text='next2')
