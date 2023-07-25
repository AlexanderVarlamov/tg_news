from aiogram import types, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from controllers.db import user_is_present, add_user
from controllers.processing import process_sources
from controllers.sources_dict import news_sources


router = Router()


class ButtonCallBack(CallbackData, prefix='but'):
    source: str


@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    msg = """
Привет! Это бот для агрегации последних новостей
Допустимые опции:
    /all Новости из всех источников
    /rambler Новости Рамблер
    /lenta Новости Лента.ру
    /news_ru Новости News.ru"""
    if message.chat.type == 'private':
        user_id = message.from_user.id
        if not user_is_present(user_id):
            add_user(user_id)
    await message.answer(msg)
    await cmd_buttons(message)


@router.message(Command(commands=news_sources.keys()))
async def get_all_news(message: types.Message):
    await process_sources(message)


async def cmd_buttons(message: types.Message):
    builder = InlineKeyboardBuilder()
    for source in news_sources:
        builder.add(types.InlineKeyboardButton(
            text=source,
            callback_data=ButtonCallBack(source=source).pack()
        ))
    await message.answer("Выберите источник новостей", reply_markup=builder.as_markup())


@router.callback_query(ButtonCallBack.filter())
async def process_button_up(query: types.CallbackQuery):
    cd_data: ButtonCallBack = ButtonCallBack.unpack(query.data)
    new_message = await query.message.edit_text(text='/' + cd_data.source)
    await process_sources(new_message)
    await cmd_buttons(new_message)


