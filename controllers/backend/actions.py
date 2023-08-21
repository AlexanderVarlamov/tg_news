import aiohttp
import feedparser


async def get_xml(rss_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=rss_url, ssl=False) as response:
            xml = await response.text()
    return xml


def parse_rss_for_web(xml: str):
    feed = feedparser.parse(xml)
    return [(item['title'], item['links'][0]['href']) for item in feed['entries']]


async def get_news_list(rss_url) -> list:
    xml = await get_xml(rss_url)
    titles = parse_rss_for_web(xml)
    return titles