from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot, dp, admin
from handlers import (start,
                      echo,
                      commands, quiz, game, fsm_store, webapp, group, send_products)
from db import db_main

async def on_startup(dp):
    await db_main.sql_create()


storage = MemoryStorage()
start.register_start(dp=dp)
commands.register_commands(dp=dp)
quiz.register_quiz(dp=dp)
game.register_game(dp=dp)
fsm_store.register_store(dp=dp)
# echo.register_echo(dp=dp)
webapp.register_handlers_webapp(dp)
group.register_group(dp=dp)
send_products.register_send_products_handler(dp=dp)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
