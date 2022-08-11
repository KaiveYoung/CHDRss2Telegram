import redis  as pyredis
from telegram import Bot
from instance.config import TELEGRAM_TOKEN
class TelegramBot(object):
    bot=None
    def __init__(self,app=None) -> None:
        pass

    def init_app(self,app=None):
        self.bot=Bot(TELEGRAM_TOKEN)


telegram=TelegramBot()