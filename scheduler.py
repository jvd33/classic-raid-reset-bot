from apscheduler.schedulers.asyncio import AsyncIOScheduler

from constants import Raids, Days
from data import RedisClient

scheduler = AsyncIOScheduler()

@scheduler.scheduled_job(misfire_grace_time=300, coalesce=True, trigger='cron', minute='*/5')
def poll_lockouts():
    redis = RedisClient()
    states = [redis.get_raid_reset(raid) for raid in Raids]

def verify_state():
    redis = RedisClient()
    states = [redis.get_raid_reset(raid) is not None for raid in Raids]
    if not all(states):
        recalc_lockouts()
    print('Application state verified. All raid lockouts set.')
    return True
