import random
import string
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

count = 0
HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - описание бота
/count - счетчик самого себя"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(HELP_COMMAND)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Добро пожаловать в наш Телеграмм Бот!')
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text='Данный бот является тестовым')

@dp.message_handler(commands=['count'])
async def cout_command(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count +=1

@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        return await message.reply('YES')
    await message.reply('NO')
@dp.message_handler()
async def message_answer(message: types.Message):
    if ['0', 'NO'] in message.text:
        await message.reply(text='YES')
    await message.reply(random.choice(string.ascii_letters))

if __name__ == '__main__':
    executor.start_polling(dp)