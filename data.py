import redis
import datetime
import json

from constants import Raids, Days
from settings import BotSettings

class RedisClient:

    def __init__(self, *args, **kwargs):
        self.__redis = redis.Redis(host='localhost', port=6379, db=0)

    def get_guild_config(self, guild_id: str):
        cached_settings = self.__redis.get(guild_id)
        if not cached_settings:
            return self.set_guild_config(guild_id, BotSettings.default())
        return json.loads(cached_settings)

    def set_guild_config(self, guild_id: str, conf):
        self.__redis.set(guild_id, json.dumps(conf))
        return BotSettings(**conf)
    
    def get_raid_reset(self, raid: str):
        return self.__redis.get(str(raid))

    def set_raid_reset(self, raid: str, reset_date: str):
        return self.__redis.set(str(raid), reset_date)
