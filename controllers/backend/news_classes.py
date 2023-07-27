from abc import ABC, abstractmethod

from controllers.backend.actions import lenta_ru_news, rambler_news


class NewsGetter(ABC):
    @abstractmethod
    async def get_news(self) -> list[str]:
        pass


class LentaNewsGetter(NewsGetter):
    def __init__(self, raw=False):
        self.raw = raw

    async def get_news(self):
        return await lenta_ru_news(self.raw)


class RamblerGetter(NewsGetter):
    def __init__(self, raw=False):
        self.raw = raw

    async def get_news(self):
        return await rambler_news(self.raw)


class SourceNewsGetter:
    def __init__(self, source: NewsGetter):
        self.source = source

    async def __call__(self):
        return await self.source.get_news()
