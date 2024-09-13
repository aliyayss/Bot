from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import bot, dp
from handlers import (start,
                      echo,
                      commands, quiz, game, fsm_store)

storage = MemoryStorage()
start.register_start(dp=dp)
commands.register_commands(dp=dp)
quiz.register_quiz(dp=dp)
game.register_game(dp=dp)
fsm_store.register_fsm_store(dp=dp)
echo.register_echo(dp=dp)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
