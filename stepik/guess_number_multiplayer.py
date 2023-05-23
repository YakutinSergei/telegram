import random

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text, Command

BOT_TOKKEN = '5626944524:AAG_e4YvB0jLb63T0BCt2s0zupv6zpIH0a4'

bot = Bot(BOT_TOKKEN)
dp = Dispatcher(bot)

#Количество поппыток пользователю
ATTEMPTS: int = 5

# Словарь, в котором будут храниться данные пользователя
user: dict = {}


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
    if message.from_user.id not in user:
        user[message.from_user.id] = {'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}


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
    await message.answer(f'Всего игр сыграно:'
                         f'{user[message.from_user.id]["total_games"]}\n'
                         f'Игр выиграно: {user[message.from_user.id]["wins"]}')


#Команжа CANCEL
@dp.message_handler(commands=['cancel'])
async def process_cancel_command(message: Message):
    if user[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть'
                             'снова - напишите об этом')
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')

#Готов сыграть
@dp.message_handler(text=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'])
async def process_positive_answer(message: Message):
    if not user[message.from_user.id]['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        user[message.from_user.id]['in_game'] = True
        user[message.from_user.id]['secret_number'] = get_random_number()
        user[message.from_user.id]['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')

#Отказ
@dp.message_handler(text=['Нет', 'Не', 'Не хочу', 'Не буду'])
async def process_negative_answer(message: Message):
    if not user[message.from_user.id]['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')

# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
@dp.message_handler(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if user[message.from_user.id]['in_game']:
        if int(message.text) == user[message.from_user.id]['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            user[message.from_user.id]['in_game'] = False
            user[message.from_user.id]['total_games'] += 1
            user[message.from_user.id]['wins'] += 1
        elif int(message.text) > user[message.from_user.id]['secret_number']:
            await message.answer('Мое число меньше')
            user[message.from_user.id]['attempts'] -= 1
        elif int(message.text) < user[message.from_user.id]['secret_number']:
            await message.answer('Мое число больше')
            user[message.from_user.id]['attempts'] -= 1

        if user[message.from_user.id]['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {user[message.from_user.id]["secret_number"]}\n\nДавайте '
                                 f'сыграем еще?')
            user[message.from_user.id]['in_game'] = False
            user[message.from_user.id]['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message_handler()
async def process_other_text_answers(message: Message):
    if user[message.from_user.id]['in_game']:
        await message.answer('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')




if __name__ == '__main__':
    executor.start_polling(dp) #start bot