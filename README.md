# CHDBits rss sync to telegram channel

## RUN

`docker-compose up -d`

## ENV

Set in to environment or .env file

|Parma|Description|Default|
|--|--|--|
|CELERY_BROKER| celery broker| redis://127.0.0.1:6379/0|
|REDIS_HOST| redis host | 127.0.0.1|
|REDIS_PORT|redis port |6379|
|REDIS_DB|redis db |0|
|TELEGRAM_TOKEN|telegram bot token ||
|TELEGRAM_CHATID|telegram chat id ||
|CHD_RSS|CHDBits.io rss |https://chdbits.co/torrentrss.php?rows=10|

