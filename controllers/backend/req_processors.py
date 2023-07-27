from controllers.backend.news_classes import SourceNewsGetter
from controllers.backend.sources_dict import sources


def get_sources(lst: list[str]):
    if lst == ['all']:
        news_to_get = sources.keys()
    else:
        news_to_get = [item for item in lst if item in sources.keys()]
    return news_to_get


async def process_news_request(lst: list[str]) -> list:
    news_to_get = get_sources(lst)
    news_to_return = []
    for one_source in news_to_get:
        source_getter = sources[one_source]()
        news_getter = SourceNewsGetter(source_getter)
        news_from_source = await news_getter()
        news_to_return.append({one_source: news_from_source})

    return news_to_return


async def process_raw_news_request(lst: list[str]) -> list:
    news_to_get = get_sources(lst)
    news_to_return = []
    for one_source in news_to_get:
        source_getter = sources[one_source](True)
        news_getter = SourceNewsGetter(source_getter)
        news_from_source = await news_getter()
        news_to_return.append({one_source: news_from_source})

    return news_to_return
