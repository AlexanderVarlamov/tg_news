from typing_extensions import Type

from controllers.backend.news_classes import *

sources: dict[str, NewsGetter] = {
    "lenta_ru": LentaNewsGetter(),
    "rambler": RamblerGetter(),
    "rbc": RbcNewsGetter()
}

sources_and_description = {
    "lenta_ru": "Новости lenta.ru",
    "rambler": "Новости rambler.ru",
    "rbc": "Новости rbc.ru",
    "all": "Новости из всех источников"
}