from aiogram import Bot, Dispatcher, executor, types


# бот - сервер, который будет взаимодействовать с API telegram

TOKEN_API = '5626944524:AAG_e4YvB0jLb63T0BCt2s0zupv6zpIH0a4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.count(' ') >=1:
        await message.answer(text=message.text.upper()) #написать сообщение



if __name__ == '__main__':
    executor.start_polling(dp) #start bot