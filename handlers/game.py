from config import bot, dp
from aiogram import types, Dispatcher
import random


games= ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
async def game(message: types.Message):
    text = message.text
    random_game = random.choice(games)
    await bot.send_dice(
        chat_id=message.from_user.id,
        emoji=random_game,)
def register_game(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])