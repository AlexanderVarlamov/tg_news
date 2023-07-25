from aiogram import Bot, Dispatcher
from conf import api_token
from routes.routes import router

bot = Bot(token=api_token)
dp = Dispatcher()
dp.include_router(router)