from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/help</b> = <em> показывает список команд</em>
<b>/give</b> = <em> отправляет кота</em>
<b>/start</b> = <em> запускает бота </em>
"""

async def on_startup(_):
    print('я запустился')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')



@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
#
# @dp.message_handler()
# async def count(message: types.Message):
#     await message.answer(text=str(message.text.count('✅')))



# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.answer('<em>Добро <b>пожаловать</b> в наш Телеграмм Бот!</em>', parse_mode='HTML')
#     await message.delete()
#
#
# @dp.message_handler(commands=['give'])
# async def give_command(message: types.Message):
#     await message.answer('Смотри какой смешной кот👍')
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEI9EJkXcklsxD6byp_fhN-xIczloHdGAACdhUAAsD3kEjX6E_o_CmgYy8E')
#     await message.delete()
#
# @dp.message_handler(commands=['description'])
# async def start_command(message: types.Message):
#     await message.answer('<em>Добро <b>пожаловать</b> в наш Телеграмм Бот!</em>', parse_mode='HTML')
#     await message.delete()
#
# @dp.message_handler()
# async def send_stiker(message: types.Message):
#     if message.text == '❤️':
#         await message.reply('🖤')
#         await message.delete()




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)