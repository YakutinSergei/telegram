import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
#from aiogram.filters import Text, Command


BOT_TOKEN = ''

user: dict = {
    'in_game': False,
    'secret_number': None,
    'attempts': None,
    'total_games': 0,
    'wins': 0
    }
def get_ramdom_number():
    return random.randint(1, 100)

