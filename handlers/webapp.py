from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

    geeks_online = KeyboardButton('Geeks Online',
                                  web_app=types.WebAppInfo(url='https://online.geeks.kg/'))

    youtube = KeyboardButton('YouTube',
                             web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    kinogo = KeyboardButton('Kinogo', web_app=types.WebAppInfo(url='https://kinogo.biz/'))

    ts = KeyboardButton('TS', web_app=types.WebAppInfo(url='https://www.ts.kg/'))

    limon_kg = KeyboardButton('limon.kg', web_app=types.WebAppInfo(url='https://limon.kg/ru'))

    keyboard.add(geeks_online, youtube, kinogo, ts, limon_kg)

    await message.answer(text='WebApp кнопки: ', reply_markup=keyboard)



def register_handlers_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])