import aiohttp
import feedparser


async def get_xml(rss_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=rss_url, ssl=False) as response:
            xml = await response.text()
    return xml


def parse_rss_for_web(xml: str):
    feed = feedparser.parse(xml)
    return [(item['title'], item['link']) for item in feed['entries']]


async def lenta_ru_news(raw=False) -> list:
    rss_url = "https://lenta.ru/rss/last24"
    xml = await get_xml(rss_url)
    titles = parse_rss_for_web(xml)
    return titles


async def rambler_news(raw=False) -> list:
    rss_url = "https://news.rambler.ru/rss/world/"
    xml = await get_xml(rss_url)
    titles = parse_rss_for_web(xml)
    return titles
