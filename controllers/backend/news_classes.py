from abc import ABC, abstractmethod

from controllers.backend.actions import lenta_ru_news, rambler_news, get_news_list


class NewsGetter(ABC):
    @abstractmethod
    async def get_news(self) -> list[str]:
        pass


class LentaNewsGetter(NewsGetter):
    _rss = "https://lenta.ru/rss/last24"

    async def get_news(self):
        return await get_news_list(self._rss)


class RamblerGetter(NewsGetter):
    _rss = "https://news.rambler.ru/rss/world/"

    async def get_news(self):
        return await get_news_list(self._rss)


class RbcNewsGetter(NewsGetter):
    _rss = "http://static.feed.rbc.ru/rbc/logical/footer/news.rss"

    async def get_news(self):
        return await get_news_list(self._rss)

class SourceNewsGetter:
    def __init__(self, source: NewsGetter):
        self.source = source

    async def __call__(self):
        return await self.source.get_news()
