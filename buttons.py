from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sizes = ReplyKeyboardMarkup().add(
    KeyboardButton(text='XL'),
    KeyboardButton(text='L'),
    KeyboardButton(text='M'),
    )