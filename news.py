from config import *
from newsapi import NewsApiClient                                         # news


def all_sources():
    news_api = NewsApiClient(api_key=news_api_key)
    res = []
    for x in news_api.get_sources()['sources']:
        res.append(x['id'])
    return res


def news_start(bot, update):
    update.message.reply_text('Hi! I can give you some frash news\n' + 
                            'Type /sources to get all available sources')


def news_help(bot, update):
    update.message.reply_text('Just type, for example, /news bbc-news')


def sources(bot, update):
    update.message.reply_text(all_sources())


def news(bot, update, args):
    if args == []:
        source = 'bbc-news'
    else:
        source = "".join(str(x) for x in args)
    news_api = NewsApiClient(api_key=news_api_key)
    top_headlines = news_api.get_top_headlines(sources=source)
    articles = top_headlines['articles']
    text = ''
    for article in articles:
        title = article['title'] 
        url = article['url']
        text = text + title + '\n' + url + '\n'
    update.message.reply_text(text)

