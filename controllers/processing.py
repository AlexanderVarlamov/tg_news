import unicodedata
import requests
from aiogram.enums import ParseMode
from aiogram.types import Message

from conf import backend_ip, backend_port, backend_api, internal_backend
from controllers.backend.req_processors import process_raw_news_request
from controllers.sources_dict import news_sources

NEWS_SERVER = f'http://{backend_ip}:{backend_port}{backend_api}'


def get_news_url(title, url):
    return f'<a href="{url}">{title}\n</a>'


def normalize_json(lst: list[dict]) -> list[dict]:
    for source in lst:
        for key in source.keys():
            inner_list = source[key]
            new_inner_list = [[unicodedata.normalize('NFKC', item[0]), item[1]] for item in inner_list]
            new_inner_list = [get_news_url(item[0], item[1]) for item in new_inner_list]
            source[key] = new_inner_list
    return lst


async def process_sources(message: Message):
    if internal_backend:
        raw_json = await process_raw_news_request([message.text[1:]])
    else:
        json_to_send = {"sources": [news_sources[message.text[1:]]]}
        news = requests.post(NEWS_SERVER, json=json_to_send)
        raw_json: list[dict] = news.json()['news']
    links_json = normalize_json(raw_json)
    for source in links_json:
        for key in source.keys():
            inner_list = source[key]
            await message.answer(text='\n'.join(inner_list), parse_mode=ParseMode.HTML)
