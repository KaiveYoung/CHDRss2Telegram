import os

from dotenv import load_dotenv

load_dotenv()

CELERY_BROKER=os.getenv('CELERY_BROKER', "redis://127.0.0.1:6379/1")
REDIS_HOST=os.getenv('REDIS_HOST', "127.0.0.1")
try:
    REDIS_PORT=int(os.getenv('REDIS_PORT', "6379"))
except:
    REDIS_PORT=6379
try:
    REDIS_DB=int(os.getenv('REDIS_DB', "0"))
except:
    REDIS_DB=0

CHD_RSS=os.getenv('CHD_RSS', "https://chdbits.co/torrentrss.php?rows=10")
TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHATID=os.getenv('TELEGRAM_CHATID')
