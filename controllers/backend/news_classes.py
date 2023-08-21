from abc import ABC

from controllers.backend.actions import get_news_list


class NewsGetter(ABC):
    _rss: str

    async def get_news(self) -> list[str]:
        return await get_news_list(self._rss)


class LentaNewsGetter(NewsGetter):
    _rss = "https://lenta.ru/rss/last24"


class RamblerGetter(NewsGetter):
    _rss = "https://news.rambler.ru/rss/world/"


class RbcNewsGetter(NewsGetter):
    _rss = "http://static.feed.rbc.ru/rbc/logical/footer/news.rss"


class IxbtNewsGetter(NewsGetter):
    _rss = "https://www.ixbt.com/export/news.rss"


class SourceNewsGetter:
    def __init__(self, source: NewsGetter):
        self.source = source

    async def __call__(self):
        return await self.source.get_news()
