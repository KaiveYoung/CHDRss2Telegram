import redis  as pyredis
from instance.config import REDIS_PORT,REDIS_DB,REDIS_HOST
class Redis(object):
    r=None
    def __init__(self,app=None) -> None:
        pass

    def init_app(self,app=None):
        pool = pyredis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        self.r = pyredis.Redis(connection_pool=pool)

redis=Redis()