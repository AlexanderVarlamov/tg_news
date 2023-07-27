from typing_extensions import Type

from controllers.backend.news_classes import *

sources: dict[str, Type[NewsGetter]] = {
    "lenta_ru": LentaNewsGetter,
    "rambler": RamblerGetter
}
