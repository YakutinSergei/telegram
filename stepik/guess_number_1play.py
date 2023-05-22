import random

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.filters import Text, Command

BOT_TOKKEN = '5626944524:AAG_e4YvB0jLb63T0BCt2s0zupv6zpIH0a4'

bot = Bot(BOT_TOKKEN)
dp = Dispatcher(bot)

#Количество поппыток пользователю
ATTEMPTS: int = 5

# Словарь, в котором будут храниться данные пользователя
user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0}


#Функция возвращает случайное число
def get_random_number() -> int:
    return random.randint(1,100)


#Команда START
@dp.message_handler(commands=['start'])
async def process_start_commands(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


#Команда HELP
@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')

#Команда Stat
@dp.message_handler(commands=['stat'])
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]}\n'
                         f'Игр выиграно: {user["wins"]}')


#Команжа CANCEL
@dp.message_handler(commands=['cancel'])
async def process_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть'
                             'снова - напишите об этом')
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')

#Готов сыграть
@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'], ignore_case=True))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')


if __name__ == '__main__':
    executor.start_polling(dp) #start bot