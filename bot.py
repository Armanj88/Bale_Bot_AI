from parameters import *

from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

dispatcher = Dispatcher()
session = AiohttpSession(
    api=TelegramAPIServer.from_base("https://tapi.bale.ai/"),
)
bot = Bot(token=TOKEN, session=session)
