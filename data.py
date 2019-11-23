import redis


class RedisClient:

    def __init__(self, *args, **kwargs):
        self.__redis = redis.Redis(host='redis', port=6379, db=0)

    def get_guild_config(self, guild_id: str):
        return self.__redis.get(guild_id)

    def set_guild_config(self, guild_id, conf):
        return self.__redis.set(guild_id, conf)