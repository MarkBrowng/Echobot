from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(msg: types.Message):
   await bot.send_message(msg.chat.id, msg.text)


if __name__ == '__main__':
   executor.start_polling(dp)

text = '''
git init - это инициализация
git add (name) - добавление файла в GIT
git add --all - добавление всех файлов в GIT, кроме .gitignore
    #.gitignore - файл, в котором прописаны директории и файлы, которые не отслеживаются GIToм
git commit - сохранение изменений в сохраненку
git log - выводит сохраненки
'''