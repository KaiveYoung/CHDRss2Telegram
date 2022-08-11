import datetime
import feedparser
from app.ext import redis,telegram
from pyquery import PyQuery as pq
from telegram import Bot
from time import sleep
from app import celery
from instance.config import TELEGRAM_CHATID,CHD_RSS
from urllib.parse import urlparse,parse_qsl
__all__=["chdrss"]


def human_readable_size(size, decimal_places=3):
    for unit in ['B','KB','MB','GB','TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f}{unit}"




@celery.task(name='chdrss')
def chdrss():
    rss = feedparser.parse(CHD_RSS)
    for entity in rss["entries"]:
        summary=pq(entity["summary"])
        summary("fieldset").remove()
        summary("img").remove()
        message=f'*{entity["title"]}*\n\n'
        tags=entity["tags"]
        links=entity["links"]
        url=""
        bt_url=""
        size=0
        for link in links:
            if link.get("type")=='text/html':
                url=link.get("href")
            if link.get("type")=='application/x-bittorrent':
                bt_url=link.get("href")
                size=int(link.get("length"))
            
        a=urlparse(url)
        id=dict(parse_qsl(a.query)).get("id")
        if redis.r.get(f"pushed_id_{id}") is not None:
            continue
        redis.r.set(f"pushed_id_{id}",1,ex=172800)
        size=human_readable_size(size)
        tag=','.join([f'{tag["term"]}' for tag in tags])
        message+=f'{url} [{size}]({bt_url})\n'
        message+=f'{tag}\n'
        message+=summary.text()
        if len(message)>800:
            message=message[:800]+"..."
        telegram.bot.send_message(TELEGRAM_CHATID, message,disable_web_page_preview=True,parse_mode='Markdown')
        sleep(1)
