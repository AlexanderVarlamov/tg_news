import logging

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app import bot
from conf import admin_id, internal_backend
from controllers.backend.sources_dict import sources_and_description as news_sources_int
from controllers.db import user_is_present, add_user, get_users, set_user_status
from controllers.processing import process_sources, get_greeting
from controllers.sources_dict import sources_and_description as news_sources_ext

router = Router()
news_sources = news_sources_int if internal_backend else news_sources_ext


class ButtonCallBack(CallbackData, prefix='but'):
    source: str


@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    msg = get_greeting(news_sources)
    if message.chat.type == 'private':
        user_id = message.from_user.id
        if not user_is_present(user_id):
            add_user(user_id)
    await message.answer(msg)
    await cmd_buttons(message)


@router.message(Command(commands='sendall'))
async def send_message_to_subscribers(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_id:
            text_to_send = message.text[9:]
            users = get_users()
            for row in users:
                try:
                    await bot.send_message(chat_id=row[0], text=text_to_send)
                    if not row[1]:
                        set_user_status(row[0], True)
                except Exception as e:
                    logging.warning(e)
                    set_user_status(row[0], False)


@router.message(Command(commands=news_sources.keys()))
async def get_all_news(message: types.Message):
    await process_sources(message)
    await cmd_buttons(message)


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
