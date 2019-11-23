import redis
import datetime

from constants import Raids, Days
from settings import BotSettings

class RedisClient:

    def __init__(self, *args, **kwargs):
        self.__redis = redis.Redis(host='localhost', port=6379, db=0)

    def get_guild_config(self, guild_id: str):
        return BotSettings(**self.__redis.get(guild_id))

    def set_guild_config(self, guild_id: str, conf):
        return self.__redis.set(guild_id, conf)
    
    def get_raid_reset(self, raid: str):
        return self.__redis.get(str(raid))

    def set_raid_reset(self, raid: str, reset_date: str):
        return self.__redis.set(str(raid), reset_date)
