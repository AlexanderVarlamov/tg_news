from controllers.backend.news_classes import *

sources: dict[str, NewsGetter] = {
    "lenta_ru": LentaNewsGetter(),
    "rambler": RamblerGetter(),
    "rbc": RbcNewsGetter(),
    "iXBT": IxbtNewsGetter()
}

sources_and_description = {
    "lenta_ru": "Новости lenta.ru",
    "rambler": "Новости rambler.ru",
    "rbc": "Новости rbc.ru",
    "iXBT": "Новости iXBT",
    "all": "Новости из всех источников"
}