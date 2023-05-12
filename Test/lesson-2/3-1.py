from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот был запущен')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Добро <b>пожаловать</b> в наш Телеграмм Бот!</em>', parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['give'])
async def start_command(message: types.Message):
    await message.answer('Смотри какой смешной кот👍')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEI9EJkXcklsxD6byp_fhN-xIczloHdGAACdhUAAsD3kEjX6E_o_CmgYy8E')
    await message.delete()

@dp.message_handler()
async def send_emiji(message: types.Message):
    await message.reply('🖤')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)